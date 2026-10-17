-- Quarto/Pandoc lift notes after boxes and floats. Save each mark's number and
-- Hyperref destination before another note advances either counter.
local serial = 0
local header_added = false

local function lift_notes(blocks)
  local notes = pandoc.Blocks({})
  local content = pandoc.Div(quarto.utils.as_blocks(blocks)):walk({
    Note = function(note)
      serial = serial + 1
      local id = tostring(serial)
      local content = note.content
      if content[1].t == 'Para' then
        content[1].content:insert(1, pandoc.RawInline('latex', '\\BookCalloutText{' .. id .. '}{'))
      else
        content:insert(1, pandoc.RawBlock('latex', '\\BookCalloutText{' .. id .. '}{'))
      end
      if content[#content].t == 'Para' then
        content[#content].content:insert(pandoc.RawInline('latex', '}'))
      else
        content:insert(pandoc.RawBlock('latex', '}'))
      end
      notes:extend(content)
      return pandoc.RawInline('latex', '\\BookCalloutMark{' .. id .. '}')
    end
  }).content
  if #notes > 0 and not header_added then
    quarto.doc.include_text('in-header', [[
\makeatletter
\DeclareRobustCommand{\BookCalloutMark}[1]{%
  \footnotemark
  \expandafter\xdef\csname BookNoteNumber#1\endcsname{\number\value{footnote}}%
  \expandafter\xdef\csname BookNoteHref#1\endcsname{\Hy@footnote@currentHref}}
\newcommand{\BookCalloutText}[2]{%
  \begingroup
  \edef\Hy@footnote@currentHref{\csname BookNoteHref#1\endcsname}%
  \c@footnote=\csname BookNoteNumber#1\endcsname\relax
  \footnotetext{#2}%
  \endgroup}
\makeatother
]])
    header_added = true
  end
  return content, notes
end

function Callout(node)
  if not FORMAT:match('latex') then return nil end
  local content, notes = lift_notes(node.content)
  if #notes == 0 then return nil end
  node.content = content
  local blocks = pandoc.Blocks({quarto.Callout(node)})
  blocks:extend(notes)
  return pandoc.Div(blocks)
end

function FloatRefTarget(node)
  if not FORMAT:match('latex') or not node.caption_long then return nil end
  -- Keep marks out of the list of figures and other moving short captions.
  local short = node.caption_short or pandoc.Plain(quarto.utils.as_inlines(
    pandoc.Div(quarto.utils.as_blocks(node.caption_long)):walk({Note = function() return {} end}).content))
  local content, notes = lift_notes(node.caption_long)
  if #notes == 0 then return nil end
  node.caption_long = content
  node.caption_short = short
  local blocks = pandoc.Blocks({quarto.FloatRefTarget({
    identifier = node.identifier, classes = node.classes,
    attributes = node.attributes, type = node.type, order = node.order,
    content = node.content, caption_long = content, caption_short = short
  })})
  blocks:extend(notes)
  return pandoc.Div(blocks)
end

-- Regression check (Quarto, XeLaTeX, pypdf): python3 scripts/test_pdf_footnotes.py
