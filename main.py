import fileHandler

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_path = "phase2_train_v0.csv"
    image_data_list = fileHandler.read_csv_file(file_path)

    for i, image_data in enumerate(image_data_list[:5]):
        print(f"Image {i + 1}:")
        print(f"File Name: {image_data.img_fName}")
        print(f"Width: {image_data.img_w}")
        print(f"Height: {image_data.img_h}")
        print(
            f"Bounding Box (xtl, ytl, xbr, ybr): ({image_data.bbx_xtl}, {image_data.bbx_ytl}, {image_data.bbx_xbr}, {image_data.bbx_ybr})")
        print(f"Class Label: {image_data.class_label}")
        print()
