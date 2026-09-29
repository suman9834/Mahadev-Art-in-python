<div align="center">

# 🎨 Sequential Part Draw & Fill

**Watch any image draw itself, outline by outline, color by color.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python\&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?logo=opencv\&logoColor=white)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-required-013243?logo=numpy\&logoColor=white)](https://numpy.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](./LICENSE)

<!-- Add your demo GIF or screenshot here -->

<!-- ![Demo](assets/demo.gif) -->

</div>

---

## ✨ Overview

**Sequential Part Draw & Fill** is a Python + OpenCV project that transforms a normal image into a **live drawing and color-fill animation**.

The program analyzes the image, detects different color regions, draws their boundaries one by one using a custom cursor, moves the cursor toward the center of each region, and finally fills the region with its original color.

The animation continues until the complete image is reconstructed.

The project includes `mahadev.jpg` as the default sample image, but you can use your own image as well.

---

## 🚀 Features

* 🖊️ Live outline drawing with a custom arrow cursor
* 🎯 Automatic region detection using **K-Means color segmentation**
* 🧩 Larger regions are processed before smaller details
* 🖼️ Automatic image resizing to fit the screen
* 📐 Aspect ratio is preserved during resizing
* 🧠 Connected-component analysis for identifying separate regions
* 🎨 Original image colors are restored during the fill stage
* ⌨️ Press `Esc` anytime to stop the animation
* ⚙️ Easy-to-customize segmentation, speed, filtering, and edge parameters
* 🖥️ Real-time visualization using OpenCV

---

## 🧠 How It Works

The project follows a complete computer-vision pipeline:

| Step | Process                  | What Happens                                                           |
| ---- | ------------------------ | ---------------------------------------------------------------------- |
| 1    | **Resize**               | Image is scaled to a 700 px height while preserving its aspect ratio   |
| 2    | **Preprocessing**        | Bilateral filtering smooths the image while preserving important edges |
| 3    | **Edge Detection**       | Canny detects prominent image boundaries                               |
| 4    | **Segmentation**         | K-Means groups pixels into color clusters                              |
| 5    | **Component Extraction** | Connected components are extracted from each color region              |
| 6    | **Noise Filtering**      | Very small regions under 120 px are ignored                            |
| 7    | **Sorting**              | Regions are ordered from largest area to smallest                      |
| 8    | **Outline Animation**    | The cursor progressively traces each region's boundary                 |
| 9    | **Cursor Movement**      | The cursor smoothly moves toward the region center                     |
| 10   | **Color Fill**           | The original image colors are copied into the detected region          |
| 11   | **Final Result**         | The completed image is displayed                                       |

---

## 🔬 Computer Vision Techniques

This project demonstrates several important image-processing concepts:

### 🎨 K-Means Color Segmentation

K-Means clustering divides image pixels into a predefined number of color groups.

The default value is:

```python
num_segments = 18
```

Increasing this value can produce more detailed regions, while decreasing it produces fewer and larger regions.

---

### 🔍 Canny Edge Detection

Canny edge detection is used to identify important boundaries within the image.

```python
edges = cv2.Canny(blurred, 40, 130)
```

---

### 🌫️ Bilateral Filtering

A bilateral filter is applied before edge detection to reduce noise while preserving edges:

```python
blurred = cv2.bilateralFilter(gray, 7, 60, 60)
```

---

### 🧩 Connected Components

After segmentation, connected components are used to identify individual regions.

Very small regions are ignored:

```python
if area > 120:
```

This helps reduce unnecessary noise and tiny animations.

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/suman9834/Mahadev-Art-in-python.git
cd Mahadev Art in python
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install opencv-python numpy
```

## ▶️ Usage

Make sure your image is inside the project folder.

Example:

```text
Sequential-Part-Draw-Fill/
│
├── main.py
├── mahadev.jpg
├── requirements.txt
└── README.md
```

Then run:

```bash
python main.py
```

The OpenCV window will open and the sequential drawing animation will begin.

---

## 🖼️ Using Your Own Image

Place your image inside the project directory.

For example:

```text
my_image.jpg
```

Then modify the final line of `main.py`:

```python
if __name__ == "__main__":
    part_by_part_draw_and_fill("my_image.jpg", num_segments=18)
```

You can also experiment with the number of segments:

```python
part_by_part_draw_and_fill("my_image.jpg", num_segments=25)
```

---

## 🎮 Controls

| Key     | Action                                        |
| ------- | --------------------------------------------- |
| `Esc`   | Stop the animation and close the window       |
| Any key | Close the window after the animation finishes |

---

## ⚙️ Configuration

The following parameters can be adjusted to customize the animation.

| Setting                   | Location             | Effect                                        |
| ------------------------- | -------------------- | --------------------------------------------- |
| `num_segments`            | Function argument    | Controls the number of K-Means color clusters |
| `target_height = 700`     | Inside function      | Controls the output image height              |
| `area > 120`              | Part extraction loop | Minimum region size                           |
| `range(1, len(cnt), 3)`   | Outline loop         | Controls contour drawing speed                |
| `cv2.waitKey(35)`         | Fill step            | Controls pause after each fill                |
| `Canny(blurred, 40, 130)` | Edge detection       | Controls Canny edge sensitivity               |

---

## 🎯 Recommended Settings

Different images may require different settings.

### Fewer Segments

```python
num_segments = 10
```

Useful for images with simple colors.

### Balanced

```python
num_segments = 18
```

Good starting point for most images.

### More Detail

```python
num_segments = 25
```

Can produce more regions and finer details, but may increase processing time.

---

## 📁 Project Structure

```text
Sequential-Part-Draw-Fill/
│
├── main.py
├── mahadev.jpg
├── requirements.txt
├── README.md
├── LICENSE
```

### File Description

| File               | Description                    |
| ------------------ | ------------------------------ |
| `main.py`          | Main Python/OpenCV application |
| `mahadev.jpg`      | Default sample image           |
| `requirements.txt` | Python dependencies            |
| `README.md`        | Project documentation          |
| `LICENSE`          | MIT License                    |
| `assets/demo.gif`  | Optional project demonstration |

---

## 📸 Demo

For a screenshot:

```markdown
![Project Screenshot](assets/screenshot.png)
```

A short demo GIF is especially useful because the main feature of this project is the **drawing animation**.

---

## 💡 Tips

* K-Means starts with random cluster centers, so different runs may produce slightly different segmentation.
* Images with clear and distinct colors generally produce better results.
* Large images may take longer to process.
* Increasing `num_segments` can increase processing time.
* Increasing the minimum region area can remove more small details.
* A wrong image path will raise a `FileNotFoundError`.
* The result depends heavily on the colors, background, and complexity of the input image.

---

## ⚠️ Limitations

This project uses automatic color-based segmentation, so it does not understand the semantic meaning of objects in an image.

For example, it identifies regions primarily based on **color and connectivity**, rather than knowing that a region represents a face, crown, hand, background, etc.

Results may vary for images containing:

* Complex backgrounds
* Similar colors
* Heavy textures
* Strong shadows
* Gradients
* Very small details
* Low contrast

---

## 🚀 Future Improvements

Planned or possible improvements include:

* [ ] Add pause/resume functionality
* [ ] Add drawing-speed controls
* [ ] Add interactive segmentation controls
* [ ] Add GIF export
* [ ] Add video export
* [ ] Add webcam support
* [ ] Add background removal
* [ ] Add multiple drawing animation styles
* [ ] Add progress bar
* [ ] Add GUI controls for OpenCV parameters
* [ ] Add automatic image optimization
* [ ] Add support for drag-and-drop images

---

## 🤝 Contributing

Contributions are welcome!

### 1. Fork the Repository

```bash
git fork
```

### 2. Create a Feature Branch

```bash
git checkout -b feature/my-feature
```

### 3. Commit Your Changes

```bash
git add .
git commit -m "Add my feature"
```

### 4. Push the Branch

```bash
git push origin feature/my-feature
```

### 5. Open a Pull Request

Submit a Pull Request with a short explanation of your changes.

---

## 👨‍💻 Author

**Suman Kumar**

B.Tech CSE (AI & Data Science)
Full Stack Developer | ML & Data Science Learner

### Connect With Me

* GitHub: [@suman9834](https://github.com/suman9834)
* LinkedIn: [Suman Kumar](https://www.linkedin.com/in/suman-kumar-93b1b431/)


<div align="center">

### ⭐ If you found this project interesting, consider giving it a star!

**Built with Python, OpenCV & NumPy ❤️**

</div>
