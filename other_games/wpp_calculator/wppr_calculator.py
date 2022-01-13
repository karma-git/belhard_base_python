#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class RectangularObject:
    """
    The class defines the default rectangular object:
    ├── properties:
    │    ├── x: the object length
    │    └── y: the object width
    ├── methods:
    │    ├── sqr : square of the object
    """

    def __init__(self, x, y):
        self.length = x
        self.width = y

    def sqr(self):
        """
        The method returns square of the object
        """
        return self.length * self.width


class NamedRectangularObject(RectangularObject):
    """
    The class has additional property:
    │    ├── description : name / description / location of the object
    """

    def __init__(self, x, y, d):
        RectangularObject.__init__(self, x, y)
        self.description = d


class ExcessObject(NamedRectangularObject):
    """
    The class for an object which square needs to exclude from total room square,
    due to we can not hang wallpapers on this object.
    """

    def property_dictionary(self):
        """
        The method return all properties in dict
        """
        return {'description': self.description,
                'length': self.length,
                'width': self.width,
                'square': self.sqr()}

    def __repr__(self):
        """
        Object name = self.description
        """
        return self.description


class Room(RectangularObject):
    """
    This class of methods for get calculate square for hang wallpapers
    """

    def __init__(self, x, y, z):
        RectangularObject.__init__(self, x, y)
        self.roll_sqr = WallPapers(x, y).sqr()
        self.height = z
        self.excess_sqr_list = []

    def sqr(self):
        """
        !Modified!
        The method calculates square of the rooms walls if the room is parallelepiped.
        It takes fallowing params:
        - length
        - width
        - height
        - room square (floor square)
        Returns walls square (w/o top & bottom edges)
        """
        # sqr = 2 (xy + yz + xz) # xy - bottom  & top edges
        walls_sqr = 2 * (self.length * self.height +
                         self.width * self.height)
        return walls_sqr

    def add_excess_object(self, x, y, d):
        """
        The method adds excess obj to list
        """
        self.excess_sqr_list.append(ExcessObject(x, y, d))

    def exclude_excess_object(self, d):
        """
        The method exclude excess obj from list by description
        """
        self.excess_sqr_list.remove(d)

    def excess_objects_sqr(self):
        """
        The method calculates square of all excess objects
        """
        square_list = []
        for i in self.excess_sqr_list:
            square_list.append(i.property_dictionary()['square'])
        return sum(square_list)

    def wallpapers_sqr(self):
        """
        The method calculates square for hang wallpaper
        """
        return self.sqr() - self.excess_objects_sqr()

    def roll_count(self):
        """
        The method calculates quantity of wallpapers rolls which needed to hang wallpapers in some room
        """
        return round(self.wallpapers_sqr() / self.roll_sqr, 2)


class WallPapers(RectangularObject):
    """
    This class of methods for work with wallpapers
    """
    # def roll_count(self, sqr):
    #     """
    #     The method calculates quantity of wallpapers rolls which needed to hang wallpapers in some room
    #     """
    #     return round(sqr / self.sqr(), 2)
