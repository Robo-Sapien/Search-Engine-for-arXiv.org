from scipy import spatial
import numpy


class CosineScore:
    """Calculate cosine similarity score for each document and rank them

    :param query: query vector

    :param matrix: tf-idf numpy matrix
    """
    rank = None
    docIndex = None
    score = None
    def __init__(self, query, matrix):
        self.rank = []
        self.docIndex = []
        self.score = []
        """Constructor which calculates cosine similarity score for each document"""
        for j in range(matrix.shape[1]):
            column = matrix[:,j]
            self.docIndex.append(j)
            self.score.append(1 - spatial.distance.cosine(column, query))
        self.rank = list(reversed([x for _, x in sorted(zip(self.score, self.docIndex))]))

    def getPages(self, number):
        """To get the indices of the douments between the given ranks

        :param start: starting *rank*.

        :param end: rank after the last rank.

        :return: list of document indices for ranks from start to end-1.
        """
        rankList = []
        if number > len(self.rank):
            min = len(self.rank)
        else:
            min = number
        for index in range(min):
            if self.score[self.rank[index]] > 0:
                rankList.append(self.rank[index])
        return rankList


# def main():
#     query = [0, 1, 0]
#     matrix = numpy.array([[2, 1, 3], [4, 3, 5], [6, 5, 7]])
#     obj = CosineScore(query, matrix)
#     print(obj.getPages(10))
#
# if __name__ == '__main__':
#     main()
