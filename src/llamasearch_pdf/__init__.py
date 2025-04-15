"""
LlamaSearch PDF - PDF processing tools for document processing workflows.

This package provides tools for working with PDF documents, including:
- OCR (Optical Character Recognition) for text extraction
- PDF manipulation (merging, splitting, etc.)
- PDF content extraction and text processing
- PDF metadata extraction and management
- PDF conversion to other formats
- PDF search and indexing capabilities
"""

__version__ = "0.1.0"

# Import main modules for easy access
from . import cli, core, ocr, search

# Import commonly used functions for convenient access
from .core import (  # PDF processor; Text extraction; Metadata
    MetadataManager,
    PDFProcessor,
    TextExtractor,
    create_basic_metadata,
    extract_metadata,
    extract_text,
    update_metadata,
)
from .ocr import (
    get_available_engines,
    ocr_image,
    ocr_pdf,
    process_directory,
)
from .search import (
    SearchIndex,
    SearchResult,
    create_index,
    search_pdfs,
)

# Define what gets imported with "from llamasearch_pdf import *"
__all__ = [
    "ocr",
    "core",
    "cli",
    "search",
    "PDFProcessor",
    "TextExtractor",
    "extract_text",
    "MetadataManager",
    "extract_metadata",
    "update_metadata",
    "create_basic_metadata",
    "ocr_pdf",
    "ocr_image",
    "process_directory",
    "get_available_engines",
    "SearchIndex",
    "SearchResult",
    "create_index",
    "search_pdfs",
]
