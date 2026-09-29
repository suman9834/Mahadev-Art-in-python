import cv2
import numpy as np

def draw_builtin_cursor(canvas, x, y):
    h, w, _ = canvas.shape
    pt1 = (x, y)
    pt2 = (min(w - 1, x + 16), min(h - 1, y + 16))
    pt3 = (min(w - 1, x + 5), min(h - 1, y + 20))

    cursor_shape = np.array([pt1, pt2, pt3])
    cv2.drawContours(canvas, [cursor_shape], 0, (30, 30, 30), -1)
    cv2.drawContours(canvas, [cursor_shape], 0, (255, 255, 255), 1)
    cv2.circle(canvas, pt1, 2, (0, 0, 255), -1)

def part_by_part_draw_and_fill(image_path="mahadev.jpg", num_segments=18):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError(f"'{image_path}' not found!")

    # Perfect screen fit (Height 700px taaki Windows taskbar ke upar poori fit aaye)
    orig_h, orig_w, _ = img.shape
    target_height = 700
    target_width = int(target_height * (orig_w / orig_h))
    img = cv2.resize(img, (target_width, target_height), interpolation=cv2.INTER_AREA)
    h, w, _ = img.shape

    # 1. Edges detect karna
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.bilateralFilter(gray, 7, 60, 60)
    edges = cv2.Canny(blurred, 40, 130)

    # 2. Segments (K-Means) alag alag parts nikalne ke liye
    pixel_data = np.float32(img).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    _, labels, _ = cv2.kmeans(pixel_data, num_segments, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    labels = labels.reshape((h, w))

    win_name = "Sequential Part Draw & Fill"
    cv2.namedWindow(win_name, cv2.WINDOW_AUTOSIZE)

    canvas = np.ones((h, w, 3), dtype=np.uint8) * 255
    cv2.imshow(win_name, canvas)
    cv2.waitKey(300)

    # Parts ke components identify karna
    parts = []
    for seg_id in range(num_segments):
        mask = (labels == seg_id).astype(np.uint8)
        num_labels, comp_labels, stats, centroids = cv2.connectedComponentsWithStats(mask)
        
        for c in range(1, num_labels):
            area = stats[c, cv2.CC_STAT_AREA]
            if area > 120:  # Ignore tiny noise
                part_mask = (comp_labels == c).astype(np.uint8) * 255
                cx, cy = int(centroids[c][0]), int(centroids[c][1])
                parts.append({
                    "area": area,
                    "center": (cx, cy),
                    "mask": part_mask
                })

    # Bade parts pehle (Skin/Mukut base), detail parts baad me (Tilak/Mala beads)
    parts = sorted(parts, key=lambda p: p["area"], reverse=True)
    current_pos = [w // 2, h // 2]

    # Har part ke sath sath outline + color fill loop
    for part in parts:
        p_mask = part["mask"]
        cx, cy = part["center"]

        # Step A: Sirf is hisse ki boundary outline nikalna
        contours, _ = cv2.findContours(p_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        for cnt in contours:
            if len(cnt) < 10:
                continue
            for i in range(1, len(cnt), 3):
                pt_prev = tuple(cnt[i - 1][0])
                pt_curr = tuple(cnt[i][0])
                cv2.line(canvas, pt_prev, pt_curr, (30, 30, 30), 2, cv2.LINE_AA)

                display = canvas.copy()
                draw_builtin_cursor(display, pt_curr[0], pt_curr[1])
                cv2.imshow(win_name, display)
                if cv2.waitKey(1) & 0xFF == 27:
                    cv2.destroyAllWindows()
                    return

        # Step B: Cursor smoothly is part ke center me jayega
        steps = 8
        for s in range(1, steps + 1):
            mx = int(current_pos[0] + (cx - current_pos[0]) * (s / steps))
            my = int(current_pos[1] + (cy - current_pos[1]) * (s / steps))
            display = canvas.copy()
            draw_builtin_cursor(display, mx, my)
            cv2.imshow(win_name, display)
            if cv2.waitKey(1) & 0xFF == 27:
                cv2.destroyAllWindows()
                return
        
        current_pos = [cx, cy]

        # Step C: Fill color in this specific part
        canvas[p_mask > 0] = img[p_mask > 0]

        display = canvas.copy()
        draw_builtin_cursor(display, cx, cy)
        cv2.imshow(win_name, display)
        cv2.waitKey(35)  # Color fill pause

    # Final crisp touch
    canvas[edges > 0] = (25, 25, 25)
    cv2.imshow(win_name, img)
    print("Sequential Art Complete! Press any key to exit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    part_by_part_draw_and_fill("mahadev.jpg")