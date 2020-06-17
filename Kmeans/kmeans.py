from PIL import Image
import urllib.request
import io
import sys
import random


def check_above(x, y, color, pix, img):
    if x - 1 < 0:
        if y - 1 < 0:
            return False
        return (x + 1, y - 1) in color
    elif y - 1 < 0:
        return (x - 1, y) in color
    elif x + 1 >= img.size[0]:
        return (x, y - 1) in color or (x - 1, y) in color or (x - 1, y - 1) in color
    else:
        return (x, y - 1) in color or (x - 1, y) in color or (x - 1, y - 1) in color or (x + 1, y - 1) in color


def main():
    k = int(sys.argv[1])
    file_path = sys.argv[2]
    if file_path[0:4] == 'http':
        f = io.BytesIO(urllib.request.urlopen(file_path).read())
        img = Image.open(f)
    else:
        img = Image.open(file_path)
    pix = img.load()

    # for i in range(img.size[0]):
    #     for j in range(img.size[1]):
    #         temp = pix[i, j]
    #         pix[i, j] = (0 if temp[0] < 255 // 2 else 255,
    #                      0 if temp[1] < 255 // 2 else 255,
    #                      0 if temp[2] < 255 // 2 else 255)
    # keys = set()
    # for i in range(k):
    #     saved = [0, 0, 0]
    #     for j in range(10):
    #         temp = pix[random.randint(0, img.size[0]), random.randint(0, img.size[1])]
    #         saved[0] += temp[0]
    #         saved[1] += temp[1]
    #         saved[2] += temp[2]
    #     saved[0] //= 10
    #     saved[1] //= 10
    #     saved[1] //= 10
    #     keys.add(tuple(saved))
    means = {pix[random.randint(0, img.size[0]), random.randint(0, img.size[1])]: 0 for x in range(k)}
    groupings = {key: [] for key in means.keys()}
    current = list(means.keys())
    classifications = {}
    saved = {}
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            temp = pix[i, j]
            if temp not in saved:
                saved[temp] = 1
            else:
                saved[temp] += 1
            if temp not in classifications:
                small = [(pix[i, j][0] - k[0]) ** 2 + (pix[i, j][1] - k[1]) ** 2 + (pix[i, j][2] - k[2]) ** 2 for k in
                         current]
                save = small.index(min(small))
                classifications[temp] = current[save]
            means[classifications[temp]] += 1
            groupings[classifications[temp]].append((i, j))
    lengths = [means[x] for x in means]
    count = 1
    while True:
        current = []
        for b in groupings:
            added = [0, 0, 0]
            for c in groupings[b]:
                added[0] += pix[c[0], c[1]][0]
                added[1] += pix[c[0], c[1]][1]
                added[2] += pix[c[0], c[1]][2]
            added[0] /= (means[b] * 1.0)
            added[1] /= (means[b] * 1.0)
            added[2] /= (means[b] * 1.0)
            current.append(tuple(added))
        means = {x: 0 for x in current}
        groupings = {key: [] for key in means.keys()}
        classifications = {}
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                temp = pix[i, j]
                if temp not in classifications:
                    small = [(pix[i, j][0] - k[0]) ** 2 + (pix[i, j][1] - k[1]) ** 2 + (pix[i, j][2] - k[2]) ** 2 for k
                             in
                             current]
                    save = small.index(min(small))
                    classifications[temp] = current[save]
                means[classifications[temp]] += 1
                groupings[classifications[temp]].append((i, j))
        new_lengths = [means[x] for x in means]
        difference = [lengths[x] - new_lengths[x] for x in range(len(lengths))]
        print("Generation {}: {}".format(count, difference))
        count += 1
        if set(difference) == {0}:
            break
        lengths = new_lengths
    convert = {}
    rev_convert = {}
    for b in classifications:
        convert[classifications[b]] = (
            int(classifications[b][0]), int(classifications[b][1]), int(classifications[b][2]))
        rev_convert[convert[classifications[b]]] = classifications[b]
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pix[i, j] = convert[classifications[pix[i, j]]]
    x = list(saved.keys())[0]
    max_num = x

    for i in saved:
        if saved[i] > saved[max_num]:
            max_num = i

    print(
        "Size: {} x {}\nPixels: {}\nDistinct pixel count: {}\nMost common pixel: {} => {}\nFinal means:\n".format(
            img.size[0],
            img.size[1],
            img.size[
                0] *
            img.size[1],
            len(
                classifications.keys()), max_num, saved[max_num]))
    count = 1
    for i in means:
        print("{}: {} => {}".format(count, i, means[i]))
        count += 1

    # img.save("kmeans/{}.png".format('2021aalex'), "PNG")
    img.show()

    regions = []
    for a in means:
        finished = set()
        count = 0
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if pix[i, j] == convert[a]:
                    if not check_above(i, j, finished, pix, img):
                        count += 1
                    finished.add((i, j))
        regions.append(count)
    print("Region counts: {}".format(str(regions)))


if __name__ == '__main__':
    main()
