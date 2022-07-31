# -cockroach-hide-behavior

EYESIM SIMULATOR 

Innate Releasing Mechanisms (IRM) is a specific stimulus which releases, or triggers, the stereotypical pattern of action. The IRM activates the behavior. For our assignment problem is to study cockroach hiding behavior and then design and implement a stimulation robot with cockroach hiding behavior at EyeSim platform. The cockroach exhibits a reflexive hiding behavior. This kind of insect can run away very quickly and find a niche in seconds and yet have little in the way of brains. Therefore, in our implementation, we did not have ‘Plan’, we only had ‘Sense-Act’. The cockroach hiding behavior can be described like when the light goes on in a
room with a cockroach in it, the cockroach will be scared, then it will turn and run toward the dark. If the cockroach meets a “wall,” or any other obstacle, such as a sofa, it follows the “wall” or the obstacle. This is also a taxis where the cockroach orients itself to the “wall.” When the cockroach finds a “hiding place,” it goes in and faces outward. Cockroaches are thigmotropic just like they like to be squeezed. Hence, a hiding place is one where there is pressure or contact on all sides. The cockroach then waits, even if the lights are turned back off earlier for some length of time, then comes out. This is a fixed pattern action, as the cockroach waits to resume its activities even if the original stimulus to hide like ‘the lights go on’ is removed. The cockroach hiding behavior can be decomposed into three behaviors which are flee, follow-wall, and hide. The random move of the cockroach is replaced by following the right wall. The light is substituted with an obstacle. If the cockroach sees the obstacle, it will act like it sees the light. The ‘follow-wall’ behavior is replaced by ‘follow the right wall’.
Therefore, our IRM will be as below:


![Screenshot 2022-08-01 053632](https://user-images.githubusercontent.com/55165601/182046302-2bbfe1ef-3d89-4382-a96d-52213a463ca4.png)

*Describe the task*
The robot needs to have cockroach behaviors.

*Describe the robot*
The robot that we used is the S4 robot. The sensors that will be used are camera and IR sensor.

*Describe the environment*
Due to the limitation of simulation, we cannot have a light source that is similar to real life.Therefore, we substitute the light source with other objects. Since we use an obstacle as a substitution of the light source, the obstacle used cannot be too small and must can be seen by the robot.

*Describe how the robot should act in response to its environment*
For the random movement when the cockroach is not scared, the robot will follow the right wall. If the robot sees light, then it will feel scared and go away from the light. If it feels scared and blocked, then it will follow the right ‘wall’ or obstacle. If it feels scared and surrounded, it will hide in the surrounded place. The ‘scared’ is declared as a global variable in Python.

*Implement and refine each behavior*
For behavior of flee after seeing light,
Trial 1: Use the difference between two images to capture the present of the obstacle. If the difference is big, then it has obstacles present in the image.
Trial 2: Used Mug as a substitute of the light source and used gray image taken by the camera as the sensor for the light source. The rationale of using the Mug is because the Mug is white color,therefore it will have the highest pixel value. We can use the threshold to capture the present of the Mug.
Trial 3: Since the result of Trial 2 told us that we cannot use a gray image to detect the obstacle, then we changed to a color camera. We will use a yellow cone as the obstacle as this color is different from the environment. The first layer of the image is the red layer. The second layer of the image represents the green layer. The third layer of the image represents the blue layer. Due to the lighting of the environment, the yellow color detected by the camera may change when the robot is moving, therefore, we can use a range of pixel values to detect the obstacles. The possible values for the red and green layer are 255 but the possible values for the
blue layer is a range. This is to allow the camera to accept yellow, light yellow and other yellow.

For behavior of following wall,
Trial 1: Implement logic for the robot to find the nearest wall. Then, follow it.
Trial 2: Implement right wall following.

For behavior of hiding,
Trial 1: Implement the robot to turn back when it is in the safe place where the front, left and right are blocked. Test each behavior independently
Result of Trial 1: Not successful because in the maze environment, it will have not much difference between no obstacles and having an obstacle. It has many pixel values when it captures the walls as an image. Hence, when it captures the obstacle as an image, it will have almost the same number of pixel values.
Result of Trial 2: It is difficult to implement the settings of Trial 2 because the environment of the maze has light. But we cannot turn off the light. The eyeSim did not have the setting to turn off the light, hence, the camera will detect the light from the environment as the obstacles or the substitution for the light source.
Result of Trial 3: Success

For behavior of following wall,
Trial 1: Success in individual behavior test only.
Trial 2: Success

For behavior of hiding,
Trial 1: Success
Test behaviors together. After testing together, the robot does not function well like it is tested individually.

For behavior of following the nearest wall, not success when integrating all the behavior.

3. Implementation and limitation
Coding below is to find the color

![Screenshot 2022-08-01 054229](https://user-images.githubusercontent.com/55165601/182046502-8ba4be9f-fc7d-4a12-a999-4d5f7d934769.png)

The ‘values’ variable is the pixel values of the image. The ‘values[i]’ is the pixel values for the red layer. The ‘values[i+QQVGA_PIXELS]’ is for the green layer. The
‘values[i+2*QQVGA_PIXELS] ‘ is for the blue layer. The RGB of yellow is (255,255,0). And, in eyeSim, 255 is represented as ‘-1’. Therefore, the above coding is to find yellow colour. We find the blue layer is not equal to -1 to let it accept a variety of yellow color. This is the most workable code that we have tried.


![Screenshot 2022-08-01 054425](https://user-images.githubusercontent.com/55165601/182046558-82f4af28-e2dd-47c1-98ef-5f1f75bc7e4a.png)

The figure above shows the robot has seen the yellow cone and it runs away by following the right wall. Then it faces outward and stays for 5 seconds before it continues back the following wall behavior.

*Challenges*
If the camera detects further parts, it will get brighter or higher values. It cannot differentiate whether it is the light source or it is far away only. This challenge is solved by changing the obstacle with a color that is different from the surrounding. Like yellow. For the settings of our environment, we cannot use blue obstacles, as the sky of the environment is also blue in color and we cannot use white color as there is a real light in the environment. If using the same color obstacle with the element of the environment, the robot will confuse and do not know how to differentiate it as the obstacles or the environment.

*Limitation*
The cockroach might turn in a circle when the robot is in the wall following behavior but it is not near to the wall. The cone must be right in front only the camera can detect it. If there is a similar color with the yellow or has the ‘R’ and ‘G’ values of 255, then the robot might detect it as the obstacle. Therefore, it might detect other things as obstacles or the light source. The robot might be stuck in some places.

4. Related references
https://mitpress.mit.edu/books/introduction-ai-robotics
https://stackoverflow.com/questions/14684362/negative-rgb-values
