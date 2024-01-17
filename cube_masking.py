
#masking scirpt
# this script will appy a mask on a velocity cube, make sure that the headers are similar
#the masks I generated have been from sofia 2 : https://gitlab.com/SoFiA-Admin/SoFiA-2
from astropy.io import fits

# Get user input for FITS cube and mask filenames
cube_filename = input("Enter the filename for the FITS cube: ")
mask_filename = input("Enter the filename for the mask FITS file: ")

# Load FITS file
fits_cube = fits.open(cube_filename)
cube_data = fits_cube[0].data

# Load mask file
mask_data = fits.getdata(mask_filename)

# Apply the mask to the cube data
masked_cube_data = cube_data * mask_data

# Update the data
fits_cube[0].data = masked_cube_data

# Save the new FITS file
output_filename = input("Enter the filename for the masked FITS cube: ")
fits_cube.writeto(output_filename, overwrite=True)

# Close the FITS cube file
fits_cube.close()
