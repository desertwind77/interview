#!/usr/bin/env python3
#
# https://community.topcoder.com/stat?c=problem_statement&pm=1215
#
# Problem Statement
#
# Karel is a frustrated painter who works by day in an electrical repair shop.
# Inspired by the color-coded bands on resistors, he is painting a series of long,
# narrow canvases with bold colored stripes. However, Karel is lazy and wants to
# minimize the number of brush strokes it takes to paint each canvas.
#
# Abbreviating each color to a single uppercase letter, Karel would write the stripe
# pattern red-green-blue-green-red as "RGBGR" (quotes added for clarity). It would
# take him three brush strokes to paint this pattern. The first stroke would cover
# the entire canvas in red (RRRRR). The second stroke would leave a band of red on
# either side and fill in the rest with green (RGGGR). The final brush stroke would
# fill in the blue stripe in the center (RGBGR).
#
# Given a stripe pattern stripes as a String, calculate the minimum number of brush
# strokes required to paint that pattern.
#
# Definition
# Class:	StripePainter
# Method: minStrokes
# Parameters: String
# Returns: int
# Method signature: int minStrokes(String stripes)
# (be sure your method is public)
#
# Notes
# - The blank canvas is an ugly color and must not show through.
#
# Constraints
# - stripes will contain only uppercase letters ('A'-'Z', inclusive).
# - stripes will contain between 1 and 50 characters, inclusive.
#
# Examples
# 0)
# "RGBGR"
# Returns: 3
# Example from introduction.
#
# 1)
# "RGRG"
# Returns: 3
# This example cannot be done in two strokes, even though there are only two colors.
# Suppose you tried to paint both red stripes in one stroke, followed by both green
# stripes in one stroke. Then the green stroke would cover up the second red stripe.
# If you tried to paint both green stripes first, followed the red stripes, then the
# red stroke would cover up the first green stripe.
#
# 2)
# "ABACADA"
# Returns: 4
# One long stroke in color 'A', followed by one stroke each in colors 'B', 'C', and 'D'.
#
# 3)
# "AABBCCDDCCBBAABBCCDD"
# Returns: 7
#
# 4)
# "BECBBDDEEBABDCADEAAEABCACBDBEECDEDEACACCBEDABEDADD"
# Returns: 26
