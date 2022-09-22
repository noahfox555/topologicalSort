from asyncio.windows_events import NULL
from contextlib import nullcontext
from graphlib import TopologicalSorter

WHITE = 'WHITE'
BLACK = 'BLACK'
GRAY = 'GRAY'

class node:
    color = NULL
    depth = NULL 
    name = NULL
    parent = NULL

def sortGraphList(graph):
    nodeList = []
    for key in graph:
        nodeList.append(key)
    nodeList.sort(key=lambda n: n.name)
    
    return nodeList

def DFS(graph, sortedCourseList):
    topologicalSorted = []
    depth = 0
    for course in sortedCourseList:
        course.color = WHITE
        course.depth = NULL
        course.parent = NULL
    
    stack = []
    for course in sortedCourseList:
        if (course.color == WHITE):
            stack.append(course)
        while (not len(stack) == 0):
            c = stack.pop()
            for nextCourse in graph[c]:
                # print(nextCourse.name)
                if (nextCourse.color == WHITE):
                    nextCourse.color = GRAY
                    depth = depth + 1
                    nextCourse.depth = depth
                    nextCourse.parent = c
                    stack.append(nextCourse)
            c.color = BLACK
            topologicalSorted.append(c)
    # for n in graph:
    #     print(n.depth)
    return topologicalSorted


def main():
    CPS173 = node()
    CPS173.name = 'CPS173'
    CPS111 = node()
    CPS111.name = 'CPS111'
    CPS112 = node()
    CPS112.name = 'CPS112'
    CPS242 = node()
    CPS242.name = 'CPS242'
    CPS222 = node()
    CPS222.name = 'CPS222'
    CPS261 = node()
    CPS261.name = 'CPS261'
    CPS337 = node()
    CPS337.name = 'CPS337'
    CPS342 = node()
    CPS342.name = 'CPS342'
    CPS376 = node()
    CPS376.name = 'CPS376'
    CPS377 = node()
    CPS377.name = 'CPS377'
    CPS340 = node()
    CPS340.name = 'CPS340'
    CPS37X = node()
    CPS37X.name = 'CPS37X'
    CPS375 = node()
    CPS375.name = 'CPS375'
    CPS373 = node()
    CPS373.name = 'CPS373'
    CPS371 = node()
    CPS371.name = 'CPS371'
    CPS363 = node()
    CPS363.name = 'CPS363'
    CPS367 = node()
    CPS367.name = 'CPS367'
    CPS360 = node()
    CPS360.name = 'CPS360'
    CPS372 = node()
    CPS372.name = 'CPS372'
    MAT237 = node()
    MAT237.name = 'MAT237'
    MAT109 = node()
    MAT109.name = 'MAT109'
    MAT110 = node()
    MAT110.name = 'MAT110'
    MAT111 = node()
    MAT111.name = 'MAT111'
    MAT216 = node()
    MAT216.name = 'MAT216'
    MAT229 = node()
    MAT229.name = 'MAT229'
    MAT338 = node()
    MAT338.name = 'MAT338'


    graph = {   CPS173:[],
                CPS111:[CPS112, MAT338],
                CPS112:[CPS222, CPS242, CPS261, CPS337, CPS371],
                CPS242:[CPS342],
                CPS222:[CPS340, CPS342, CPS360, CPS363, CPS367, CPS373, CPS375, CPS376, CPS377, CPS37X],
                CPS261:[CPS363],
                CPS337:[],
                CPS342:[],
                CPS376:[],
                CPS377:[],
                CPS340:[],
                CPS37X:[],
                CPS375:[],
                CPS373:[],
                CPS371:[],
                CPS363:[],
                CPS367:[],
                CPS360:[],
                CPS372:[],
                MAT237:[CPS261, CPS337, CPS367],
                MAT109:[CPS222, MAT110, MAT237],
                MAT110:[MAT111, MAT216],
                MAT111:[MAT229],
                MAT216:[CPS360, CPS372],
                MAT229:[MAT338],
                MAT338:[],
    }

    sortedListOfCourses = sortGraphList(graph)
    topologicalSortedList = DFS(graph, sortedListOfCourses)

    finalList = []
    for n in topologicalSortedList:
        finalList.append((n.name, n.depth))

    print(finalList)

main()