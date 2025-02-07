# **Turtle Graphics Programs**

This repository contains multiple Python programs utilizing the `turtle` module for interactive and creative graphical outputs.

---

## **Turtle Race**

### **Description**

The Turtle Race program creates six turtles in different colors and lets them race across the screen. The user can place a bet on which turtle will win before the race starts.

### **Features**

- **User Input:** The user places a bet on a turtle color.
- **Randomized Movement:** Each turtle moves forward randomly.
- **Race Completion:** Displays a message on whether the user's bet was correct.

### **How to Run**

1. Ensure you have Python installed.
2. Run the script:
   ```sh
   python race.py
   ```
3. Enter your bet in the pop-up prompt.
4. Watch the race and see if your turtle wins!

---

## **Sketch Program**

### **Description**

The Sketch program allows the user to control a turtle on the screen using arrow keys. The turtle can move forward, backward, and rotate, creating sketches dynamically.

### **Features**

- **Arrow Key Controls:** Move the turtle in different directions.
- **Canvas Reset:** Press `C` to reset the drawing.
- **Black Background & White Turtle:** A simple visual design for clarity.

### **How to Run**

1. Ensure you have Python installed.
2. Run the script:
   ```sh
   python sketch.py
   ```
3. Use the following keys to control the turtle:
   - **Up Arrow:** Move forward.
   - **Down Arrow:** Move backward.
   - **Left Arrow:** Turn counterclockwise.
   - **Right Arrow:** Turn clockwise.
   - **C Key:** Reset the canvas.

---

## **Heroes Program**

### **Description**

The Heroes program draws a dashed turtle path and generates a random hero name using the `heroes` module.

### **Features**

- **Dashed Turtle Path:** Alternates between pen-up and pen-down movement.
- **Random Hero Name:** Prints a randomly generated hero name.

### **How to Run**

1. Ensure you have Python installed.
2. Install the required dependency:
   ```sh
   pip install heroes
   ```
3. Run the script:
   ```sh
   python heroes.py
   ```

---

## **Shapes Program**

### **Description**

The Shapes program draws different polygons with random colors, from triangles to nonagons.

### **Features**

- **Dynamic Shape Drawing:** Draws polygons with increasing sides.
- **Random Colors:** Assigns a random color to each shape.

### **How to Run**

1. Ensure you have Python installed.
2. Run the script:
   ```sh
   python shapes.py
   ```

---

## **Spirograph Program**

### **Description**

The Spirograph program creates a colorful spirograph pattern by rotating a circle incrementally.

### **Features**

- **Smooth Animated Drawing:** Uses `turtle.speed('fastest')` for smooth execution.
- **Random Colors:** Generates RGB colors dynamically.

### **How to Run**

1. Ensure you have Python installed.
2. Run the script:
   ```sh
   python spiro.py
   ```

---

## **Random Walk Program**

### **Description**

The Random Walk program moves the turtle in random directions while changing colors.

### **Features**

- **Random Movements:** Turns the turtle randomly in 90-degree increments.
- **Dynamic Colors:** Changes color randomly for each segment.

### **How to Run**

1. Ensure you have Python installed.
2. Run the script:
   ```sh
   python walk.py
   ```

---

## **Requirements**

These programs require **Python 3** and the `turtle` module. The `heroes` program also requires:

```sh
pip install heroes
```
