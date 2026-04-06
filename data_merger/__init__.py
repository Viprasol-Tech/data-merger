"""
data-merger - Merge datasets intelligently

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import DataMerger, merge, process, main

__all__ = ["DataMerger", "merge", "process", "main"]
