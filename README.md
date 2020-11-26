# image_project

- I want to create a grid of images of height 110 and variable width such that max width never goes above 1050.

## Issues:
- When I try to resize the width to fit the image, I get image named resize_pillow_concat_tile_resize.tiff which has variable sizes of images
- But, when I try to not resize, I get pillow_concat_tile_resize.tiff where each row doesn't cover max_width. 
  - component sizes in pillow_concat_tile_resize.tiff are fine but rows do not cover max_width
