# Image-processing
Image Processing algorithms (histogram equalization, distance transformation)

## How to run
1. download image and code
  - git cloen https://github.com/99kenny/Image-processing
<br>
2. edit PATH variable to your image PATH
<br>
3. Run python file
<br>
## Histogram Equalization
- Comparison Between using CV2 lib
  - Original image<br>
  ![image](https://user-images.githubusercontent.com/57697721/226885477-eba1c617-4620-4821-a64c-f004ff7dce30.png)
  - Equalized image<br>
  ![image](https://user-images.githubusercontent.com/57697721/226885513-415bcd12-5919-40b4-a1fe-0eed54392ce4.png)
- Histogram
  - Original Histogram<br>
![image](https://user-images.githubusercontent.com/57697721/226885744-b56049cd-3238-47f1-800a-dab459af02bb.png)
  - Equalized Histogram<br>
![image](https://user-images.githubusercontent.com/57697721/226885829-13acfc6d-4689-487f-b6c6-a2c7dda214ab.png)
<br>
You can check that by equalizing the histogram, the contrast of the image has been enchanced

## Distance Transformation
- Comparison Between using CV2 lib
  - Original image<br>
  ![image](https://user-images.githubusercontent.com/57697721/226886955-fa1f7509-790e-42f2-9507-38a958975565.png)
  - Transformed image
    - D4<br>
    ![image](https://user-images.githubusercontent.com/57697721/226887141-8b34e1e1-aecf-4601-948d-1216c65b9504.png)
    - D8 <br>
    ![image](https://user-images.githubusercontent.com/57697721/226887074-c2a938ba-3360-451d-bf39-07de0859c565.png)
    - Euclidean<br>
    ![image](https://user-images.githubusercontent.com/57697721/226887112-12a016a9-2122-4349-a3eb-b0c99ac7ecb2.png)
<br>
You can apply different distance metric by changing the 'dm' value to d4, d8, eucliden_d.

