from simple_image_download import simple_image_download as sim

response = sim.simple_image_download()

keywords =['person wearing mask','without  mask']


for i in keywords:
    response.download(i,15)