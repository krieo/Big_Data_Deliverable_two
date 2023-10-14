import fileHandler

num_aegypti = 0
num_albopictus = 0
num_anopheles = 0
num_culex = 0
num_culiseta = 0
num_japonicus_koreicus = 0

if __name__ == '__main__':
    file_path = "phase2_train_v0.csv"
    image_data_list = fileHandler.read_csv_file(file_path)

    for i, image_data in enumerate(image_data_list):
        print(f"Image {i + 1}:")
        print(f"File Name: {image_data.img_fName}")
        print(f"Width: {image_data.img_w}")
        print(f"Height: {image_data.img_h}")
        print(
            f"Bounding Box (xtl, ytl, xbr, ybr): ({image_data.bbx_xtl}, {image_data.bbx_ytl}, {image_data.bbx_xbr}, {image_data.bbx_ybr})")
        print(f"Class Label: {image_data.class_label}")
        print()
        if image_data.class_label == "aegypti":
            num_aegypti += 1
        elif image_data.class_label == "albopictus":
            num_albopictus += 1
        elif image_data.class_label == "anopheles":
            num_anopheles += 1
        elif image_data.class_label == "culex":
            num_culex += 1
        elif image_data.class_label == "culiseta":
            num_culiseta += 1
        else:
            num_japonicus_koreicus += 1


print(num_aegypti)
print(num_albopictus)
print(num_anopheles)
print(num_culex)
print(num_culiseta)
print(num_japonicus_koreicus)
sum = num_aegypti + num_albopictus + num_anopheles + num_culex + num_culiseta + num_japonicus_koreicus
print(sum)
