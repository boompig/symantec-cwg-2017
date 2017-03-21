import javaobj

fname = "user_data.ser"
marshaller = javaobj.JavaObjectUnmarshaller(open(fname))
pobj = marshaller.readObject()
print(pobj)
print(pobj.__dict__)
