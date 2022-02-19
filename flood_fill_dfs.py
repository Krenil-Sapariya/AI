def floodfill(image, sr, sc, newColor):
    # determine lengths
    row, col = len(image), len(image[0])

    # get the startColor
    startColor = image[sr][sc]

    # startColor color is same as newColor then no need to change
    if startColor == newColor:
        return image

    def dfs(i, j):
        # pick given starting pixel
        if image[i][j] == startColor:

            # change color
            image[i][j] = newColor

            # explore dfs 
            if i > 0:
                dfs(i-1, j)
            if j > 0:
                dfs(i, j-1)
            if i+1 < row:
                dfs(i+1, j)
            if j+1 < col:
                dfs(i, j+1)

    dfs(sr, sc)
    return image

if __name__ == '__main__':
 
    # imagerix showing portion of the screen having different colors
    image = [[1,1,1],[1,1,0],[1,0,1]]
 
    # start node
    x,y = 1,1
 
    # newColor color
    newColor = 2
 
    # replace the startColor color with a newColor
    result = floodfill(image, x, y, newColor)
 
    # print the colors after replacement
    print(result)