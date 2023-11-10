import lzf
import re
import xml.dom.minidom

# Copy the save file to this directory.
# Change the line below to reflect the file name (without the .xml extension).
filename = "Test"


def loadparts(skipContent = False):
    with open(filename + ".xml", mode="rb") as f:
        file = f.readlines()
        size = int(file[4].strip().decode("utf-8").replace("DataSize:=", ""))
        header = ""
        content = b""
        for i, line in enumerate(file):
            if i <= 12:
                header += line.decode("utf-8")
            else:
                content += line

        if skipContent:
            return [ header, '' ]

        content = lzf.decompress(content, size).decode('utf-8')
        dom = xml.dom.minidom.parseString(content)
        content_pretty = dom.toprettyxml()

        return [header, content_pretty]


def loadfile():
    [_, content] = loadparts(False)
    with open(filename + ".xml_editable", mode="w", encoding='utf-8') as f:
        f.write(content)


def savefile():
    [header, _] = loadparts(True)
    with open(filename + ".xml_editable", mode="r") as f:
        file = f.read()
        sf_length = len(file)
        content = lzf.compress(file)
        sfc_length = len(content)
        header = re.sub(r"^(DataSize:=)\d*", f"\\g<1>{sf_length}", header, flags=re.MULTILINE)
        header = re.sub(r"^(SaveDataSize:=)\d*", f"\\g<1>{sfc_length}", header, flags=re.MULTILINE)
        with open(filename + ".xml_new", mode="wb+") as f:
            f.write(bytes(header, "utf-8"))
            f.write(content)
        print(f"DataSize: {sf_length} SaveDataSize: {sfc_length}")

# uncomment this to create the ..._editable file.
#loadfile()

# uncomment this to convert the ..._editable file to the ..._new file.
#savefile()
