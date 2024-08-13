from PIL import Image, ImageDraw, ImageFont

# Load the handwriting font
font_path = "Pacifico-Regular.ttf"  # Update with the path to your font file
font_size = 50
font = ImageFont.truetype(font_path, font_size)

# Create a blank image with white background
image_size = (800, 400)  # You can adjust the size based on your needs
image = Image.new('RGB', image_size, color=(255, 255, 255))

# Initialize ImageDraw
draw = ImageDraw.Draw(image)

# Define the text and position
text = "my name is awadhesh here we generate"
text_position = (5,50)  # Adjust the position based on your needs

# Draw the text on the image
draw.text(text_position, text, font=font, fill=(0, 0, 0))  # Black text color

# Save or display the image
image.show()  # This will open the image
image.save("handwritten_text.png")  # Save the image
