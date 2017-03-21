import javaobj
from argparse import ArgumentParser
from pprint import pprint

def modify_with_admin(pobj):
    # print("new python object")
    pobj.is_admin = True
    # print(pobj.__dict__)

def save_new_file(outfile):
    marshaller = javaobj.JavaObjectMarshaller(open(outfile, "w"))
    marshaller.write_object(pobj)
    print ("wrote to %s" % outfile)

def modify_with_new_params(pobj, username, password, id):
    if username:
        pobj.username = username
    if password:
        pobj.password = password
    if id:
        pobj.id = id

def read_object(infile):
    marshaller = javaobj.JavaObjectUnmarshaller(open(infile))
    pobj = marshaller.readObject()
    return pobj

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("infile")
    parser.add_argument("-o", "--outfile", required=False)

    parser.add_argument("--username", required=False)
    parser.add_argument("--password", required=False)
    parser.add_argument("--id", required=False)

    args = parser.parse_args()

    pobj = read_object(args.infile)

    print("old python object:")
    print(pobj)
    pprint(pobj.__dict__)

