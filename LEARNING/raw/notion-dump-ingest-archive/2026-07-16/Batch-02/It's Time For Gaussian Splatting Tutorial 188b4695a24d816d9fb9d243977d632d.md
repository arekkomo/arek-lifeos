# It's Time For Gaussian Splatting // Tutorial

Tags: AI Video
URL: https://youtube.com/watch?v=ERuRMOVO58Q&si=iuUJgO_yEjGpYnS_
Date Added: January 27, 2025 11:23 AM
Type: Youtube
Archive: No
Spark: No

### **Summary**

*The transcript describes a detailed tutorial on a rendering technique called "Gaussian Splatting," which involves creating highly realistic 3D scenes by leveraging point clouds, Gaussian blur, and spherical harmonics. The tutorial covers the entire process, from extracting frames from a video or photos to creating and refining the Gaussian Splats, cleaning up unnecessary data, and rendering the results in software like Blender or specialized tools. It also discusses exporting and importing the results, adding lighting, and creating camera animations for further customization.*

---

### **Key Takeaways**

- **Gaussian Splatting Technique**: This method uses Gaussian blur applied to point clouds to synthesize realistic 3D scenes. It works well with reflections, transmissions, and depth information derived from 3D point clouds.

- **Preparation Process**: The process begins with extracting clean frames from a video or photo dataset, followed by camera tracking, creating a sparse point cloud, and optimizing the placement of Gaussian shards during a training phase.

- **Training Phase**: The training involves iterative refinement over thousands of steps to minimize error and produce a realistic representation of the scene. Overtraining can lead to diminishing returns.

- **Software Utilized**: The tutorial highlights the use of specialized software like Post Shot for Gaussian Splatting, Blender for further editing, and other add-ons like "3D Gaussian Splatting" or "3DGS Render" for importing and manipulating the data in Blender.

- **Cleaning and Optimization**: The scene can be cleaned by removing unnecessary or stray points using tools like selection or crop boxes. This reduces file size and improves visual accuracy.

- **Rendering in Blender**: Gaussian Splats can be imported into Blender, but Blender natively supports only point clouds, not Gaussian Splats. Add-ons are required to recreate the Gaussian Splat effect in Blender.

- **Lighting and Refinement**: The tutorial explains how to add lighting and adjust spherical harmonics to control the realism and view-dependent behavior of the Splats.

- **Camera Animation**: Camera animations can be exported from Blender and imported back into the Gaussian Splatting software for more complex rendering.

- **Export and File Size**: The final Gaussian Splat model is highly portable, with relatively small file sizes compared to traditional 3D models, making it efficient for rendering.

- **Rendering Output**: The final render can be exported as a video or image sequence directly from the Gaussian Splatting software or Blender.

- **Practical Tips**: The tutorial emphasizes the importance of balancing training steps, avoiding over-cleaning to preserve reflections and details, and leveraging add-ons for smoother workflows.