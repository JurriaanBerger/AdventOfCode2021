import numpy as np

def read_paper():
    file = open('paper.txt', "r")
    f1 = file.read()
    file.close()
    f2 = f1.split("\n")
    print(f2)

    max_x = 0
    max_y = 0

    for f in f2:
        xy = f.split(",")
        if int(xy[0]) > max_x: max_x = int(xy[0])
        if int(xy[1]) > max_y: max_y = int(xy[1])

    paper_input = np.zeros([max_y+1,max_x+1])

    for g in f2:
        xy = g.split(",")
        paper_input[int(xy[1]), int(xy[0])] = 1

    return paper_input


def fold_y(paper):
    print(paper.shape)
    new_paper = np.zeros([int((paper.shape[0]-1)/2),paper.shape[1]])

    for i in range(0,int((paper.shape[0]-1)/2)):
        for j in range(0,paper.shape[1]):
            new_paper[i, j] = paper[i, j]
            new_paper[i, j] = new_paper[i,j] + paper[(paper.shape[0]-1)-i, j]
            if new_paper[i, j] > 1: new_paper[i, j] = 1

    print(new_paper)
    return new_paper


def fold_x(paper):
    # print(paper.shape)
    new_paper = np.zeros([paper.shape[0], int((paper.shape[1] - 1) / 2)])

    for i in range(0, paper.shape[0]):
        for j in range(0, int((paper.shape[1] - 1) / 2)):
            new_paper[i, j] = paper[i, j]
            new_paper[i, j] = new_paper[i, j] + paper[i, (paper.shape[1] - 1) - j]
            if new_paper[i, j] > 1: new_paper[i, j] = 1

    print(new_paper)
    return new_paper


full_paper = read_paper()


# Part 1
fold_paper = fold_y(full_paper)
fold_paper_2 = fold_x(full_paper)
print('ANSWER 1:', np.sum(fold_paper_2))


# Part 2
paper0 = full_paper
paper1 = fold_x(paper0) # 655
paper2 = fold_y(paper1) # 447
paper3 = fold_x(paper2) # 327
paper4 = fold_y(paper3) # 223
paper5 = fold_x(paper4) # 163
paper6 = fold_y(paper5) # 111
paper7 = fold_x(paper6) # 81
paper8 = fold_y(paper7) # 55
paper9 = fold_x(paper8) # 40
paper10 = fold_y(paper9) # 27
paper11 = fold_y(paper10) # 13
paper12 = fold_y(paper11) # 6
print(paper12)