import { runAppleScript } from "run-applescript";

const CONFIG = {
  MAX_REMINDERS: 50,
  MAX_LISTS: 20,
  TIMEOUT_MS: 8000,
};

interface ReminderList {
  name: string;
  id: string;
}

interface Reminder {
  name: string;
  id: string;
  body: string;
  completed: boolean;
  dueDate: string | null;
  listName: string;
  completionDate?: string | null;
  creationDate?: string | null;
  modificationDate?: string | null;
  remindMeDate?: string | null;
  priority?: number;
}

async function checkRemindersAccess(): Promise<boolean> {
  try {
    await runAppleScript(`tell application "Reminders" to return name`);
    return true;
  } catch (error) {
    console.error(`Cannot access Reminders app: ${error instanceof Error ? error.message : String(error)}`);
    return false;
  }
}

async function requestRemindersAccess(): Promise<{ hasAccess: boolean; message: string }> {
  try {
    const hasAccess = await checkRemindersAccess();
    if (hasAccess) return { hasAccess: true, message: "Reminders access is already granted." };
    return {
      hasAccess: false,
      message: "Reminders access is required. Please open System Settings > Privacy & Security > Automation and enable Reminders.",
    };
  } catch (error) {
    return { hasAccess: false, message: `Error checking access: ${error instanceof Error ? error.message : String(error)}` };
  }
}

// Single fast AppleScript that returns all incomplete reminders as "listName|||reminderName" strings
async function fetchAllIncompleteReminders(): Promise<string[]> {
  // Use "whose completed is false" to filter at AppleScript level — avoids iterating 294 completed items
  const script = `
tell application "Reminders"
  set out to {}
  repeat with L in lists
    set n to name of L
    set activeRems to (reminders of L whose completed is false)
    repeat with r in activeRems
      set end of out to n & "|||" & name of r
    end repeat
  end repeat
  return out
end tell`;
  const result = (await runAppleScript(script)) as any;
  const arr = Array.isArray(result) ? result : result ? [result] : [];
  return arr.filter((x: any) => typeof x === "string");
}

async function getAllLists(): Promise<ReminderList[]> {
  try {
    // One-liner — fastest possible AppleScript for list names
    const result = (await runAppleScript(`tell application "Reminders" to return name of every list`)) as any;
    const arr = Array.isArray(result) ? result : result ? [result] : [];
    return arr.map((name: string) => ({ name: name || "Untitled", id: name || "" }));
  } catch (error) {
    console.error(`Error getting lists: ${error instanceof Error ? error.message : String(error)}`);
    return [];
  }
}

async function getAllReminders(listName?: string): Promise<Reminder[]> {
  try {
    const rows = await fetchAllIncompleteReminders();
    const reminders: Reminder[] = rows
      .filter((x) => x.includes("|||"))
      .map((x) => {
        const sep = x.indexOf("|||");
        return {
          name: x.slice(sep + 3),
          id: "",
          body: "",
          completed: false,
          dueDate: null,
          listName: x.slice(0, sep),
        };
      });
    return listName ? reminders.filter((r) => r.listName === listName) : reminders;
  } catch (error) {
    console.error(`Error getting reminders: ${error instanceof Error ? error.message : String(error)}`);
    return [];
  }
}

async function searchReminders(searchText: string): Promise<Reminder[]> {
  try {
    if (!searchText || searchText.trim() === "") return [];
    const all = await getAllReminders();
    const lower = searchText.toLowerCase();
    return all.filter((r) => r.name.toLowerCase().includes(lower));
  } catch (error) {
    console.error(`Error searching reminders: ${error instanceof Error ? error.message : String(error)}`);
    return [];
  }
}

async function createReminder(
  name: string,
  listName: string = "Reminders",
  notes?: string,
  dueDate?: string,
): Promise<Reminder> {
  try {
    const accessResult = await requestRemindersAccess();
    if (!accessResult.hasAccess) throw new Error(accessResult.message);
    if (!name || name.trim() === "") throw new Error("Reminder name cannot be empty");

    const cleanName = name.replace(/"/g, '\\"');
    const cleanListName = listName.replace(/"/g, '\\"');
    const script = `
tell application "Reminders"
  try
    set targetList to missing value
    repeat with L in lists
      if name of L is "${cleanListName}" then
        set targetList to L
        exit repeat
      end if
    end repeat
    if targetList is missing value then
      return "ERROR:List not found: ${cleanListName}"
    end if
    make new reminder at targetList with properties {name:"${cleanName}"}
    return "SUCCESS:${cleanListName}"
  on error errorMessage
    return "ERROR:" & errorMessage
  end try
end tell`;

    const result = (await runAppleScript(script)) as string;
    if (result && result.startsWith("SUCCESS:")) {
      return {
        name,
        id: "created-reminder-id",
        body: notes || "",
        completed: false,
        dueDate: dueDate || null,
        listName: result.replace("SUCCESS:", ""),
      };
    }
    throw new Error(`Failed to create reminder: ${result}`);
  } catch (error) {
    throw new Error(`Failed to create reminder: ${error instanceof Error ? error.message : String(error)}`);
  }
}

interface OpenReminderResult {
  success: boolean;
  message: string;
  reminder?: Reminder;
}

async function openReminder(searchText: string): Promise<OpenReminderResult> {
  try {
    const accessResult = await requestRemindersAccess();
    if (!accessResult.hasAccess) return { success: false, message: accessResult.message };

    const matchingReminders = await searchReminders(searchText);
    if (matchingReminders.length === 0) return { success: false, message: "No matching reminders found" };

    await runAppleScript(`tell application "Reminders" to activate`);
    return { success: true, message: "Reminders app opened", reminder: matchingReminders[0] };
  } catch (error) {
    return { success: false, message: `Failed to open reminder: ${error instanceof Error ? error.message : String(error)}` };
  }
}

async function getRemindersFromListById(listId: string, props?: string[]): Promise<any[]> {
  try {
    // listId may be a name in our simplified implementation
    return await getAllReminders(listId);
  } catch (error) {
    console.error(`Error getting reminders by list ID: ${error instanceof Error ? error.message : String(error)}`);
    return [];
  }
}

export default {
  getAllLists,
  getAllReminders,
  searchReminders,
  createReminder,
  openReminder,
  getRemindersFromListById,
  requestRemindersAccess,
};
