import av

container = av.open("bigbuckbunny1080p.mp4")

for frame in container.decode(video=0):
    print(frame.index)
    image = frame.to_image()
    object_methods = [method_name for method_name in dir(image) if callable(getattr(image, method_name))]
    print(image.__class__.__name__)
    print(object_methods)
    image2 = image.resize((320,200))
    image3 = image2.convert('L')
    image3.save('output/frame-small-bw-%04d.jpg' % frame.index)
