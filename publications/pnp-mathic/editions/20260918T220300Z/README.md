# Problem No Problem — locked paginated edition

Author: Virgil Lee Gattenby

The authoritative presentation is `Problem_No_Problem_Paginated.pdf`: an unnumbered splash and numbered pages 1–17. This archive preserves the audited edition exactly as approved for archive and lock.

`Problem_No_Problem_Layout_Source.docx` is the editable layout source. Its cover and PDF-only page numbers, contents links, and bookmarks require the finalization step; opening the DOCX alone is not an exact preview of the final PDF. `Rendered_Source.pdf` and `Splash.pdf` preserve the rendering inputs. Run `python3 finalize_pdf.py` in this directory with PyMuPDF and python-docx installed to produce `Rebuilt_Paginated.pdf`. For a changed DOCX, first render it to replace `Rendered_Source.pdf`, then finalize and audit as a new edition.

Lock means a checksum-frozen edition, not a mathematical certification or a repository permission setting. Future edits belong in a successor edition; do not overwrite this archive. `LOCK.json` records scope and retained layout observations. `SHA256SUMS.json` covers every archived payload other than itself.

The current PDF has Figure 1 on page 2, Figure 2 on page 4, §4.1 on page 9, Figure 3 on page 12, Figure 4 on page 15, and all references on page 17. Section 5 display formulas are 11 pt. All four figures retain their original proportions. No duplicate Appendix A has been introduced.
