from manim import *

class BinarySearchScene(Scene):
    def construct(self):
        # Create the array
        array = [1, 3, 5, 7, 9, 11, 13, 15]
        blocks = VGroup(*[Rectangle(width=1, height=1) for _ in range(len(array))])
        blocks.arrange(RIGHT, buff=0.5)
        for i, block in enumerate(blocks):
            block_text = Text(str(array[i]), font_size=24).move_to(block.get_center())
            block.add(block_text)
        self.add(blocks)

        # Initialize low, mid, and high indices
        low = 0
        high = len(array) - 1
        target = 9

        # Step 1: Initial search space
        low_index = blocks[low]
        high_index = blocks[high]
        self.add(low_index.copy().set_color(YELLOW), high_index.copy().set_color(YELLOW))
        low_arrow = Arrow(low_index.get_left(), low_index.get_center(), buff=0.1).set_color(YELLOW)
        high_arrow = Arrow(high_index.get_right(), high_index.get_center(), buff=0.1).set_color(YELLOW)
        self.add(low_arrow, high_arrow)
        low_text = Text("Low", font_size=18).next_to(low_index, DOWN)
        high_text = Text("High", font_size=18).next_to(high_index, DOWN)
        self.add(low_text, high_text)
        self.wait(1)

        while low <= high:
            mid = (low + high) // 2
            mid_index = blocks[mid]

            # Highlight mid index
            mid_index_copy = mid_index.copy().set_color(RED)
            self.add(mid_index_copy)
            mid_arrow = Arrow(mid_index.get_center(), mid_index.get_center(), buff=0.1).set_color(RED)
            self.add(mid_arrow)
            mid_text = Text("Mid", font_size=18).next_to(mid_index, DOWN)
            self.add(mid_text)
            self.wait(1)

            # Compare target with mid element
            if array[mid] == target:
                # Target found
                self.add(Text("Target found!", font_size=24).move_to(UP * 2))
                self.wait(1)
                break
            elif array[mid] < target:
                # Update low index
                low = mid + 1
                low_index = blocks[low]
                low_index_copy = low_index.copy().set_color(YELLOW)
                self.add(low_index_copy)
                low_arrow = Arrow(low_index.get_left(), low_index.get_center(), buff=0.1).set_color(YELLOW)
                self.add(low_arrow)
                low_text = Text("Low", font_size=18).next_to(low_index, DOWN)
                self.add(low_text)
                self.remove(high_index.copy(), high_arrow, high_text)
                high = mid - 1
                high_index = blocks[high]
                high_index_copy = high_index.copy().set_color(YELLOW)
                self.add(high_index_copy)
                high_arrow = Arrow(high_index.get_right(), high_index.get_center(), buff=0.1).set_color(YELLOW)
                self.add(high_arrow)
                high_text = Text("High", font_size=18).next_to(high_index, DOWN)
                self.add(high_text)
                self.wait(1)
            else:
                # Update high index
                high = mid - 1
                high_index = blocks[high]
                high_index_copy = high_index.copy().set_color(YELLOW)
                self.add(high_index_copy)
                high_arrow = Arrow(high_index.get_right(), high_index.get_center(), buff=0.1).set_color(YELLOW)
                self.add(high_arrow)
                high_text = Text("High", font_size=18).next_to(high_index, DOWN)
                self.add(high_text)
                self.remove(low_index.copy(), low_arrow, low_text)
                low = mid + 1
                low_index = blocks[low]
                low_index_copy = low_index.copy().set_color(YELLOW)
                self.add(low_index_copy)
                low_arrow = Arrow(low_index.get_left(), low_index.get_center(), buff=0.1).set_color(YELLOW)
                self.add(low_arrow)
                low_text = Text("Low", font_size=18).next_to(low_index, DOWN)
                self.add(low_text)
                self.wait(1)

            # Remove mid index highlight
            self.remove(mid_index_copy, mid_arrow, mid_text)

        self.wait(2)