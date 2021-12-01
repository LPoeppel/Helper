import glob
import os
import extract_msg

def wrtAtt(filename, data):
    print( "[i] Saving Attachment: \"" + str(filename) + "\"")
    try:
        newfile = open(filename, "wb")
        newfile.write(data)
        newfile.close
    except:
        print("[!] Error: Permisison denied! Couldn't write: \"" + str(filename) + "\".")

def getAttList(msg_file):
    print( "[i] Getting Attachments for: \"" + str(msg_file)[2:] +"\"")
    msg = extract_msg.Message(msg_file)
    att = msg.attachments
    return att
            
def main():
    path = "./"
    od = "output"
    os.path.exists(od) or os.makedirs(od)
    msg_files = glob.glob(path + "*.eml.msg")
    for msg_file in msg_files:
        attList = getAttList(msg_file)
        for element in attList:
            filename = od + "/" + element.longFilename
            data = element.data
            wrtAtt(filename, data)

if __name__ == "__main__":
    main()