---
name: localization-and-i18n
description: |
  Thiết kế và kiểm tra ngôn ngữ/locale cho website từ content model, URL, locale routing,
  typography, layout, language switcher đến SEO hreflang. Dùng không chỉ khi website có
  từ hai locale trở lên, mà còn khi một site single-locale có target language rõ ràng
  (ví dụ `html[lang="vi"]`) và cần ngăn UI bị code-switching ngoài chủ đích.
---

# Localization & Internationalization

## Separate concerns

- **i18n**: architecture cho nhiều locale.
- **l10n**: content/culture adaptation cho locale cụ thể.
- **language coherence**: mọi generic UI string của một surface phải tuân theo locale contract, kể cả site chỉ có một locale.

Không hardcode text trong reusable component nếu project dùng translation layer.

## Resolve the language contract first

Trước khi thiết kế hoặc QA copy:

1. Xác định primary locale / target language từ requirement, `html[lang]`, product docs hoặc existing content contract.
2. Ghi rõ phần nào bắt buộc theo locale: navigation, headings, helper text, buttons, form labels, validation, empty/error/success states, accessibility labels và interaction-generated copy.
3. Ghi rõ ngoại lệ được phép giữ nguyên: brand/product/proper names, established domain vocabulary, technical abbreviations hoặc legal text theo requirement.
4. Không tự biến một ngoại lệ thuật ngữ thành lý do để code-switch cả câu hay cả navigation.

Nếu target locale chưa rõ và việc chọn sai sẽ làm thay đổi public-facing product copy, phải resolve trước khi ship.

## Content rules

- UI copy phải có stable key và context.
- Không concatenate fragments khiến grammar sai khi dịch.
- Placeholder variables phải rõ nghĩa.
- Date/time/number/currency dùng locale-aware formatter.
- Không giả định English text length.
- Interaction-generated copy phải theo cùng language contract với static HTML.
- Copy trong shared chrome phải được coi là shared-owner content: header, nav, search, footer, modal, toast, status và global actions không được lệch locale so với page body.

## Language coherence hard gate

Nếu một page/surface khai báo locale, generic UI copy phải nhất quán với locale đó.

Ví dụ với `html[lang="vi"]`, các trạng thái sau là **release blocker** nếu không có ngoại lệ được document:

- navigation tiếng Anh nhưng content chính tiếng Việt;
- `Step 1 of 4`, `Continue`, `Back`, `Add to cart` xen giữa một journey tiếng Việt;
- static copy đã dịch nhưng toast/validation/empty/result state vẫn tiếng Anh;
- page title/meta/accessibility label quan trọng lệch ngôn ngữ khỏi UI chính;
- component migrated từ version cũ giữ lại copy ngôn ngữ cũ dù style đã đổi.

Không được kết luận “language QA passed” chỉ vì source HTML trông đúng. Với UI sinh bằng JavaScript hoặc stateful flow, phải render và exercise các state có tạo copy.

## Layout resilience

Test với text dài hơn 30–50%:

- Buttons không cắt label.
- Nav không overflow âm thầm.
- Cards không phụ thuộc fixed height vô lý.
- Heading wrap vẫn đẹp.
- Form label/error không phá grid.

Sau localization phải render lại vì thay đổi độ dài câu có thể tạo layout regression dù locale đúng.

## Vietnamese-specific checks

- Font phải có đầy đủ Vietnamese glyphs/diacritics.
- Line-height đủ cho dấu.
- Uppercase/letter-spacing không làm giảm readability.
- Search/sort nếu có phải xử lý Unicode đúng.
- Dấu tiếng Việt không bị mất do font fallback, text-transform hoặc copy pipeline.
- Không dùng tiếng Anh generic chỉ để “trông sang”; luxury tone không phải lý do phá language coherence.

## Locale routing

Chọn strategy nhất quán: path/domain/subdomain theo product requirement. Language switcher nên đưa user tới **equivalent page** khi có, không luôn reset về homepage.

Với single-locale site không cần dựng routing đa ngôn ngữ giả tạo. Vẫn phải enforce primary language contract.

## SEO

- Unique localized title/description.
- Correct canonical cho từng locale.
- hreflang chỉ khi thực sự có equivalent localized pages.
- Sitemap/links phải crawlable.

## Translation completeness

Không release locale có menu dịch nhưng content chính/validation/error/legal vẫn lẫn ngôn ngữ nếu không chủ đích.

Audit tối thiểu phải gồm:

- shared chrome;
- representative content pages;
- primary decision flow;
- forms + validation;
- empty/error/success states;
- generated recommendation/result states;
- operational surfaces nếu cùng product locale.

## Verification pattern

Khi project đủ phức tạp, ưu tiên một rendered language-coherence gate:

1. mở representative routes ở target locale;
2. thu visible strings sau render;
3. exercise stateful interactions tạo copy mới;
4. allowlist proper nouns/domain terms đã document;
5. fail trên generic UI phrase lệch locale;
6. lưu screenshot + machine-readable report làm evidence.

Heuristic text scan chỉ là hỗ trợ; không thay thế human review cho câu code-switch tinh vi hoặc thuật ngữ domain.

## Output

Nếu site multilingual, tạo `docs/localization-strategy.md` gồm locale list, route model, fallback, translation ownership, content fields và QA matrix.

Nếu site single-locale nhưng có language contract quan trọng, ghi contract + documented exceptions trong project truth/content strategy và nối nó vào final QA/release gate.

## Acceptance criteria

- [ ] Primary locale / target language được xác định rõ.
- [ ] Generic UI copy nhất quán với locale trên shared chrome và critical journeys.
- [ ] Interaction-generated states đã được audit, không chỉ static source.
- [ ] Proper noun/domain exceptions được document thay vì ad-hoc code-switching.
- [ ] Locale routing xác định khi project thực sự multilingual.
- [ ] Components chịu được text expansion.
- [ ] Dates/numbers/currency locale-aware.
- [ ] Language switcher preserve context khi có.
- [ ] Metadata/hreflang plan đúng với scope.
- [ ] Font glyphs locale được test.
- [ ] Rendered QA không còn accidental mixed-language release blocker.
