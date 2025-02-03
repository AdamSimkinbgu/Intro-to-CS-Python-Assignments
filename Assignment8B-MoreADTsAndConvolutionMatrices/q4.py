###################################### ---Q4--- ######################################
import matplotlib.pyplot as plt


def display(image):
    plt.imshow(image, cmap="gist_gray")
    plt.show()


def read_image(pathway):
    try:
        f = open(pathway, "r")
        f.close()
    except FileNotFoundError:
        print("The pathway is not correct")
    else:
        output_image = []
        with open(pathway, "r") as file:
            for line in file:
                to_add = [int(item) for item in line.rstrip("\n").split(" ")]
                output_image.append(to_add)
        return output_image


def edge_detection(image_nested_list, x_matrix, y_matrix):
    """
    This method is given an image and a matrix to evaluate the edges of the picture with. The assignment was for sobel
    kernel. Calculates each pixel and creates a new matrix for each convolution with the calculated edges in it.
    To achieve this, the size, the size from the middle point, the length and height of each matrix is calculated
    and then used to determine the loop sizes. In case of an off set matrix (for example a 3x4 or any larger), an
    index error is caught and passed. By that the indexes out of bounds are not calculated.
    Though... the result are kind of weird and there is no documentation online regarding non-square matrices.
    This question... is the bain of my existence. The main reason why I descend into madness... slowly but surely...
    :param image_nested_list [list[lists]] - A given image in form of BMP.
    :param x_matrix [list[lists]] - A given x matrix to calculate by.
    :param y_matrix [list[lists]] - A given y matrix to calculate by.
    :return [list[lists]] - A calculated result of the inputs. Actual output is a printed plot using matplotlib.

    @todo :  Add the resolution of the initial picture and the final picture.
    """
    x_matrix_size_ver = len(x_matrix)
    x_matrix_size_hor = len(x_matrix[0])
    matrix_x_ver = x_matrix_size_ver // 2
    matrix_x_hor = x_matrix_size_hor // 2

    y_matrix_size_ver = len(y_matrix)
    y_matrix_size_hor = len(y_matrix[0])
    matrix_y_ver = y_matrix_size_ver // 2
    matrix_y_hor = y_matrix_size_hor // 2

    res_hor = len(image_nested_list[0])
    res_ver = len(image_nested_list)
    Gx = []
    Gy = []
    G = []
    index = 0
    for k in range(3):
        for i in range(res_ver):
            row = []
            for j in range(res_hor):
                row.append(0)
            if k == 0:
                Gx.append(row)
            if k == 1:
                Gy.append(row)
            if k == 2:
                G.append(row)

    for row in range(matrix_x_ver, res_ver - matrix_x_ver):
        for col in range(matrix_x_hor, res_hor - matrix_x_hor):
            local_square = [image_nested_list[row - matrix_x_ver + i][col - matrix_x_ver: col + matrix_x_ver + 1] for i in range(x_matrix_size_ver)]
            pixel_total_x = 0
            for ver in range(x_matrix_size_ver - matrix_x_ver + 1):
                for hor in range(x_matrix_size_hor - matrix_x_hor + 1):
                    try:
                        pixel_total_x += (local_square[ver][hor] * x_matrix[ver][hor])
                    except Exception as e:
                        # index += 1
                        # print(e, 'num:',index, f'pixel {ver}: {hor}')
                        pass
            Gx[row][col] = pixel_total_x

    for row in range(matrix_y_ver, res_ver - matrix_y_ver):
        for col in range(matrix_y_hor, res_hor - matrix_y_hor):
            local_square = [image_nested_list[row - matrix_y_ver + i][col - matrix_y_ver: col + matrix_y_ver + 1] for i in range(y_matrix_size_ver)]
            pixel_total_y = 0
            for ver in range(y_matrix_size_ver - matrix_y_ver + 1):
                for hor in range(y_matrix_size_hor - matrix_y_hor + 1):
                    try:
                        pixel_total_y += (local_square[ver][hor] * y_matrix[ver][hor])
                    except Exception as e:
                        # index += 1
                        # print(e, 'num:', index, f'pixel {ver}: {hor}')
                        pass
            Gy[row][col] = pixel_total_y

    for row in range(max(matrix_x_ver, matrix_y_ver), res_ver - max(matrix_x_ver, matrix_y_ver)):
        for col in range(max(matrix_x_hor, matrix_y_hor), res_hor - max(matrix_x_hor, matrix_y_hor)):
            G[row][col] = ((Gx[row][col] ** 2 + Gy[row][col] ** 2) ** 0.5)

    return G



    # x_matrix_size = len(x_matrix)
    # temp_x_ver = x_matrix_size // 2
    # temp_x_hor = x_matrix_size[0] // 2
    #
    # y_matrix_size = len(y_matrix)
    # temp_y = y_matrix_size // 2
    # temp_y_hor = y_matrix_size[0] // 2
    #
    # res_hor = len(image_nested_list[0])
    # res_ver = len(image_nested_list)
    # GG = []
    #
    # for i in range(res_ver):
    #     row = []
    #     for j in range(res_hor):
    #         row.append(0)
    #     GG.append(row)
    # for row in range(temp_y, res_ver - temp_y):
    #     for col in range(temp_x_ver, res_hor - temp_x_ver):
    #         local_square = [image_nested_list[row - temp_x_ver + i][col - temp_y: col + temp_y + 1] for i in range(x_matrix_size)]
    #         pixel_total_x = 0
    #         pixel_total_y = 0
    #         for ver in range(y_matrix_size - temp_y + 1):
    #             for hor in range(x_matrix_size - temp_x_ver + 1):
    #                 pixel_total_x += (local_square[ver][hor] * x_matrix[ver][hor])
    #                 pixel_total_y += (local_square[ver][hor] * y_matrix[ver][hor])
    #         GG[row][col] = ((pixel_total_x ** 2 + pixel_total_y ** 2) ** 0.5)//1
    # return GG


SanFrancisco_image = read_image("SanFrancisco.txt")
display(SanFrancisco_image)
x_structure = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
y_structure = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
# SanFrancisco_post_ED_image = edge_detection(SanFrancisco_image, x_structure, y_structure)
# display(SanFrancisco_post_ED_image)



# def apply_kernel(image, kernel):
#     # Step 1
#     image_height, image_width = len(image), len(image[0])
#     result = [[0 for j in range(image_width)] for i in range(image_height)]
#     # Step 2
#     kernel_height, kernel_width = len(kernel), len(kernel[0])
#     padding_height = int((kernel_height - 1) / 2)
#     padding_width = int((kernel_width - 1) / 2)
#     padded_image = [[0 for j in range(image_width + padding_width * 2)] for i in range(image_height + padding_height * 2)]
#     # Step 3
#     for i in range(image_height):
#         for j in range(image_width):
#             padded_image[i + padding_height][j + padding_width] = image[i][j]
#     # Step 4
#     for i in range(padding_height, image_height + padding_height):
#         for j in range(padding_width, image_width + padding_width):
#             sum = 0
#             for k in range(kernel_height):
#                 for l in range(kernel_width):
#                     sum += padded_image[i - padding_height + k][j - padding_width + l] * kernel[k][l]
#             result[i - padding_height][j - padding_width] = sum
#     # Step 5
#     for i in range(image_height):
#         for j in range(image_width):
#             result[i][j] = max(0, min(255, result[i][j]))
#     # Step 6
#     plt.imshow(result, cmap='gray')
#     plt.show()

def apply_kernel(image, x_kernel, y_kernel):
    # Step 1
    image_height, image_width = len(image), len(image[0])
    x_result = [[0 for j in range(image_width)] for i in range(image_height)]
    y_result = [[0 for j in range(image_width)] for i in range(image_height)]

    # Step 2
    x_kernel_height, x_kernel_width = len(x_kernel), len(x_kernel[0])
    y_kernel_height, y_kernel_width = len(y_kernel), len(y_kernel[0])
    x_padding_height = int((x_kernel_height - 1) / 2)
    x_padding_width = int((x_kernel_width - 1) / 2)
    y_padding_height = int((y_kernel_height - 1) / 2)
    y_padding_width = int((y_kernel_width - 1) / 2)
    padded_image = [[0 for j in range(image_width + max(x_padding_width, y_padding_width) * 2)] for i in range(image_height + max(x_padding_height, y_padding_height) * 2)]

    # Step 3
    for i in range(image_height):
        for j in range(image_width):
            padded_image[i + max(x_padding_height, y_padding_height)][j + max(x_padding_width, y_padding_width)] = image[i][j]

    # Step 4
    for i in range(max(x_padding_height, y_padding_height), image_height + max(x_padding_height, y_padding_height)):
        for j in range(max(x_padding_width, y_padding_width), image_width + max(x_padding_width, y_padding_width)):
            x_sum = 0
            y_sum = 0
            for k in range(x_kernel_height):
                for l in range(x_kernel_width):
                    x_sum += padded_image[i - x_padding_height + k][j - x_padding_width + l] * x_kernel[k][l]
            for k in range(y_kernel_height):
                for l in range(y_kernel_width):
                    y_sum += padded_image[i - y_padding_height + k][j - y_padding_width + l] * y_kernel[k][l]
            x_result[i - x_padding_height][j - x_padding_width] = x_sum
            y_result[i - y_padding_height][j - y_padding_width] = y_sum

    # Step 5
    for i in range(image_height):
        for j in range(image_width):
            x_result[i][j] = max(0, min(255, x_result[i][j]))
            y_result[i][j] = max(0, min(255, y_result[i][j]))

    result = [[0 for j in range(image_width)] for i in range(image_height)]
    for i in range(image_height):
        for j in range(image_width):
            result[i][j] = int((x_result[i][j] ** 2 + y_result[i][j] ** 2)**0.5)

    max_val = max(max(result))
    for i in range(image_height):
        for j in range(image_width):
            result[i][j] = int((result[i][j] / max_val) * 255)

    # Step 6
    plt.imshow(x_result, cmap='gray')
    plt.show()
    plt.imshow(y_result, cmap='gray')
    plt.show()
    display(result)



# Example usage
image = [[0, 255, 0], [255, 0, 255], [0, 255, 0]]
x_kernel = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
y_kernel = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
apply_kernel(SanFrancisco_image, x_structure, y_structure)

