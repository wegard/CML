import pypandoc

output = pypandoc.convert_file(
    "AI_for_finans.md", "pdf", outputfile="AI_for_finans_draft.pdf"
)
