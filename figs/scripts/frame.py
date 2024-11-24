from PIL import Image, ImageDraw

# Dimensions
large_rect_width = 1280
large_rect_height = 720
small_rect_height = 16
num_small_rects = 45

# Calculate the spacing and dimensions of small rectangles
spacing = (large_rect_height - num_small_rects * small_rect_height) / (num_small_rects + 1)
small_rect_width = large_rect_width  # Add padding from edges if needed

# Create a blank image
image = Image.new("RGB", (large_rect_width + 2, large_rect_height + 2), "white")
draw = ImageDraw.Draw(image)

# Draw the large rectangle (optional border for clarity)
draw.rectangle([(0, 0), (large_rect_width, large_rect_height)], outline="black", width=2)

# Draw the smaller rectangles
for i in range(num_small_rects):
    y_top = spacing * (i + 1) + small_rect_height * i
    y_bottom = y_top + small_rect_height
    x_left = 0  # Adjust padding on the left
    x_right = x_left + small_rect_width
    if 1 <= i + 1 <= 5:
        fill_color = 'lightsalmon'
        outline_color = 'red'
    else:
        fill_color='lightblue'
        outline_color = 'darkred'
    draw.rectangle([(x_left, y_top), (x_right, y_bottom)], outline=outline_color, fill=fill_color)

# Save or display the image
image.show()  # Display the image
image.save("rectangles.png")  # Save the image
