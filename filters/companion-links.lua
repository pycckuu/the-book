-- Keep companion-file links clickable in HTML. PDF and EPUB readers use the
-- named files supplied with the source bundle, rather than missing local URIs.
function Link(link)
  if not (FORMAT:match('latex') or FORMAT:match('epub')) then return nil end
  local target = link.target
  if target:match('^%a[%w+.-]*:') or target:match('^#') then return nil end
  local path = target:gsub('[?#].*$', '')
  local extension = path:match('%.([%w]+)$')
  if not ({md=true,qmd=true,csv=true,json=true,tsv=true,py=true,zip=true})[extension] then return nil end
  local name = path:match('[^/]+$') or path
  if pandoc.utils.stringify(link.content) == name then return pandoc.Code(name) end
  local content = link.content
  content:insert(pandoc.Str(' ('))
  content:insert(pandoc.Code(name))
  content:insert(pandoc.Str(')'))
  return pandoc.Span(content)
end
