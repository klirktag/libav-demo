import av

container = av.open("bigbuckbunny1080p.mp4")

def methods_from_object(the_object):
    # Found here
    # https://stackoverflow.com/questions/34439/finding-what-methods-a-python-object-has
    object_methods = [method_name for method_name in dir(the_object) if callable(getattr(the_object, method_name))]
    return object_methods

def class_name(the_object):
    # Solution found here
    # https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
    return image.__class__.__name__

for frame in container.decode(video=0):
    print(frame.index)
    image = frame.to_image()
    object_methods = methods_from_object(image)
    print(class_name(image))
    print(object_methods)
    image2 = image.resize((320,200))
    image3 = image2.convert('L')
    image3.save('output/frame-small-bw-%04d.jpg' % frame.index)
