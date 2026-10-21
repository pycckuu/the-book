-- Layout only: let long companion filenames and automatically sized tables wrap.
function Code(code)
  if FORMAT:match('latex') and code.text:match('^[%w_./-]+%.[%w]+$') then
    return pandoc.RawInline('latex', '\\nolinkurl{' .. code.text .. '}')
  end
end

function Table(tbl)
  if not FORMAT:match('latex') then return nil end
  -- This syllabus table otherwise becomes three unwrapped natural-width columns.
  if #tbl.colspecs == 3 and pandoc.utils.stringify(tbl):find('Planned minutes', 1, true) then
    local specs = tbl.colspecs
    local widths = {0.33, 0.20, 0.47}
    for index, spec in ipairs(specs) do spec[2] = widths[index] end
    tbl.colspecs = specs
    return tbl
  end
end

function Math(math)
  if FORMAT:match('latex') and math.mathtype == 'DisplayMath'
      and math.text:match('^%s*\\Xi_%+=') then
    local text = math.text:gsub(',\\quad%s*', ',\\\\\n'):gsub('^%s+', ''):gsub('%s+$', '')
    math.text = '\\begin{gathered}\n' .. text .. '\n\\end{gathered}'
    return math
  end
end
