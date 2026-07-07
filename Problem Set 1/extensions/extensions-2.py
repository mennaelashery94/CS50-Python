def main():
    file_name = input("File name: ")
    print(file(file_name))

def file(f):
    f = f.lower().strip().split('.')

    match f[-1]:
        case "gif":
            return f"image/gif"

        case "jpg" | "jpeg":
            return f"image/jpeg"

        case "png":
            return f"image/png"

        case "pdf":
            return f"application/pdf"

        case "txt":
            return f"text/plain"

        case "zip":
            return f"application/zip"

        case _:
            return f"application/octet-stream"


main()
