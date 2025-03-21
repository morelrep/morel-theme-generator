import shutil
import os

src = '../../../_site/abouts/site-description.html'
dst = '../../../_includes/site-description.html'

print(shutil.copyfile(src, dst))