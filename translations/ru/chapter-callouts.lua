-- PDF callout boxes lift multiple footnotes with the same final counter.
-- Use an indented sidebar so each note stays attached to its own mark.
function Callout(node)
  if not FORMAT:match('latex') then return nil end
  local blocks = pandoc.Blocks({})
  if node.title then
    blocks:insert(pandoc.Para({pandoc.Strong(quarto.utils.as_inlines(node.title))}))
  end
  blocks:extend(quarto.utils.as_blocks(node.content))
  return pandoc.BlockQuote(blocks)
end
