{{- /*
  One program rendered as clean Markdown for LLMs: key facts, body and official
  links, without site chrome. Used by the per-page Markdown output
  (/programs/<slug>/index.md) and by /llms-full.txt.
  Expects dict:
  - page:  the program Page
  - level: heading level of the program title (1 for its own page, 2 inside llms-full.txt)
  - body:  include the full body (false → facts and links only)
*/ -}}
{{- $p := .page -}}
{{- $seo := partial "program-seo.html" $p -}}
{{- $h := strings.Repeat .level "#" -}}
{{- $body := "" -}}
{{- if .body -}}
  {{- $body = $p.RawContent -}}
  {{- /* "**\ " is a CJK emphasis-closing escape (see hugo.toml); plain "**" reads fine for LLMs. */ -}}
  {{- $body = replace $body "**\\ " "**" -}}
  {{- /* Root-relative links → absolute, so they still resolve outside the site. */ -}}
  {{- $body = replace $body "](/" (printf "](%s" site.BaseURL) -}}
  {{- /* Body headings start at "##"; demote them so they stay one level below the program title. */ -}}
  {{- with sub .level 1 -}}
    {{- $body = replaceRE `(?m)^(#{1,5}) ` (printf "%s$1 " (strings.Repeat . "#")) $body -}}
  {{- end -}}
{{- end -}}
{{ $h }} {{ $seo.title }}
{{ with $p.Params.subtitle }}
> {{ . }}
{{ end }}
- 상태: {{ $seo.statusLabel }} (`{{ $p.Params.status }}`)
{{- with $p.Params.open_date }}
- 접수시작: {{ (time .).Format "2006. 1. 2." }}
{{- end }}
{{- if $p.Params.deadline }}
- 접수마감: {{ $seo.deadlineText }}
{{- else if $p.Params.deadline_note }}
- 일정: {{ $p.Params.deadline_note }}
{{- end }}
{{- with $p.Params.amount }}
- 지원규모: {{ . }}
{{- end }}
{{- with $p.Params.target }}
- 지원대상: {{ . }}
{{- end }}
{{- with $p.Params.duration }}
- 사업기간: {{ . }}
{{- end }}
{{- with $p.Params.org_eu }}
- 유럽측 기관: {{ . }}
{{- end }}
{{- with $p.Params.org_kr }}
- 한국측 기관: {{ . }}
{{- end }}
{{- with $p.Params.apply_via }}
- 신청 경로: {{ . }}
{{- end }}
{{- with $p.Params.verified }}
- 최종 확인일: {{ . }}
{{- end }}
- 웹 페이지: {{ $p.Permalink }}
{{ with $body }}
{{ trim . "\n" }}
{{ end }}
{{- with $p.Params.links }}
{{ $h }}# 공식 링크 · 출처
{{ range . }}
- [{{ .name }}]({{ .url }})
{{- end }}
{{ end }}
