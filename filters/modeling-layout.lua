-- Layout only: let long companion filenames and automatically sized tables wrap.
function Code(code)
  if FORMAT:match('latex') and code.text:match('^[%w_./-]+%.[%w]+$') then
    return pandoc.RawInline('latex', '\\nolinkurl{' .. code.text .. '}')
  end
end

function Table(tbl)
  if not FORMAT:match('latex') then return nil end
  local specs = tbl.colspecs
  local unspecified = true
  for _, spec in ipairs(specs) do
    if spec[2] > 0 then unspecified = false end
  end
  if unspecified and #specs > 0 then
    for _, spec in ipairs(specs) do spec[2] = 1 / #specs end
    tbl.colspecs = specs
    return tbl
  end
end
