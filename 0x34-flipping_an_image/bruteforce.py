#!/usr/bin/env python3
class Solution:
    def flip_image(self, image: list) -> list:
        """
        Flips an image and returns the flipped image
        The image is passed in form of a list of 0s and 1s
        To flip the image means to reverse this list
        """
        if len(image) <= 1:
            return image
        left_pointer = 0
        right_pointer = len(image) - 1
        while left_pointer < right_pointer:
            temp = image[left_pointer]
            image[left_pointer] = image[right_pointer]
            image[right_pointer] = temp
            left_pointer += 1
            right_pointer -= 1
        return image
    
    def invert_image(self, image: list) -> list:
        """
        Inverts an image and returns the inverted image
        The image is passed in form of a list of 0s and 1s
        To invert an image means changing all 0s to 1s and all 1s to 0s
        """
        for i in range(0, len(image)):
            if image[i] == 0:
                image[i] = 1
            elif image[i] == 1:
                image[i] = 0
        return image

    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in range(0, len(image)):
            image[i] = self.flip_image(image[i])
            image[i] = self.invert_image(image[i])
        return image

solution = Solution()
# print(solution.flip_image([1, 1, 0, 0, 1]))
# print(solution.invert_image([1, 1, 0, 0]))
print(solution.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
print(solution.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
