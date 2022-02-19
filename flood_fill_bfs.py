from collections import deque
 
# check if it is possible to go to pixel (x, y) from the current pixel.
# The function returns false if the pixel has a different color, or it's not a valid pixel
def isSafe(image, x, y, startColor):
    return 0 <= x < len(image) and 0 <= y < len(image[0]) and image[x][y] == startColor
 
# Flood fill using BFS
def floodfill(image, x, y, newColor):
 
    # base-condition
    if not image or not len(image):
        return
 
    # create a queue to store BFS sequence
    q = deque()
    # append starting pixel
    q.append((x, y))
 
    # get the startColor color
    startColor = image[x][y]
 
    # startColor color is same as newColor then no need to change
    if startColor == newColor:
        return image
 
    # loop through all bfs sequence elements
    while q:
 
        # pick pixel from queue
        x, y = q.popleft()
 
        # replace the current pixel color with newColor
        image[x][y] = newColor

        # process all adjecent pixels
        if isSafe(image, x-1, y-1, startColor):
            q.append((x-1,y-1))

        if isSafe(image, x-1, y, startColor):
            q.append((x-1,y))

        if isSafe(image, x-1, y+1, startColor):
            q.append((x-1,y+1))

        if isSafe(image, x, y-1, startColor):
            q.append((x,y-1))

        if isSafe(image, x, y+1, startColor):
            q.append((x,y+1))

        if isSafe(image, x+1, y-1, startColor):
            q.append((x-1,y-1))

        if isSafe(image, x+1, y, startColor):
            q.append((x-1,y))

        if isSafe(image, x+1, y+1, startColor):
            q.append((x-1,y+1))

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