
### All LL API calls in sublime.py
# sublime_api.func()

active_window() #no returns?
architecture() #returns same as hl api
buffers() #no returns?
cache_path() #returns same as hl api
channel() #returns same as hl api
decode_value(data) #return val,err
encode_value(val, pretty) #returns same as hl api
error_message(msg) #no returns? #no returns?
executable_path() #returns same as hl api
expand_variables(val, variables) #returns same as hl api
find_resources(pattern) #returns same as hl api
find_syntax_for_file(path, first_line) #returns same as hl api
get_clipboard(size_limit) #returns same as hl api
get_clipboard_async(callback, size_limit) #no returns?
get_log_build_systems() #returns same as hl api
get_log_commands() #returns same as hl api
get_log_control_tree() #returns same as hl api
get_log_fps() #returns same as hl api
get_log_indexing() #returns same as hl api
get_log_input() #returns same as hl api
get_log_result_regex() #returns same as hl api
get_macro() #returns same as hl api
get_syntax(path) #returns same as hl api
html_sheet_set_contents(self.sheet_id, contents) #no returns?
installed_packages_path() #returns same as hl api
list_syntaxes() #returns same as hl api
load_binary_resource(name) #return bytes
load_resource(name) #return s
load_settings(base_name) #return settings_id
log_build_systems(flag) #no returns?
log_commands(flag) #no returns?
log_control_tree(flag) #no returns?
log_fps(flag) #no returns?
log_indexing(flag) #no returns?
log_input(flag) #no returns?
log_message(b) #no returns?
log_result_regex(flag) #no returns?
message_dialog(msg) #no returns?
ok_cancel_dialog(msg, title, ok_title) #returns same as hl api
open_dialog(file_types, directory or '', flags, cb) #no returns?
packages_path() #returns same as hl api
platform() #returns same as hl api
run_command(cmd, args) #no returns?
save_dialog(file_types, directory or '', name or '', extension or '', callback) #no returns?
save_settings(base_name) #no returns?
score_selector(scope_name, selector) #returns same as hl api
select_folder_dialog(directory or '', multi_select, cb) #no returns?
set_clipboard(text) #returns same as hl api
set_timeout(f, timeout_ms) #no returns?
set_timeout_async(f, timeout_ms) #no returns?
status_message(msg) #no returns?
ui_info() #returns same as hl api
version() #returns same as hl api
windows() #no returns?
yes_no_cancel_dialog(msg, title, yes_title, no_title) #returns same as hl api

buffer_file_name(self.buffer_id) #return name
buffer_primary_view(self.buffer_id) #no returns?
buffer_views(self.buffer_id) #no returns?

settings_add_on_change(self.settings_id, tag, callback) #no returns?
settings_clear_on_change(self.settings_id, tag) #no returns?
settings_erase(self.settings_id, key) #no returns?
settings_get(self.settings_id, key) #return res
settings_get(self.settings_id, key) #returns same as hl api
settings_get_default(self.settings_id, key, default) #returns same as hl api
settings_has(self.settings_id, key) #returns same as hl api
settings_has(self.settings_id, key): #return bool
settings_set(self.settings_id, key, value) #no returns?
settings_to_dict(self.settings_id) #returns same as hl api

sheet_close(self.sheet_id, on_close) #no returns?
sheet_file_name(self.sheet_id) #return fn
sheet_group(self.sheet_id) #return group_num
sheet_is_semi_transient(self.sheet_id) #returns same as hl api
sheet_is_transient(self.sheet_id) #returns same as hl api
sheet_set_name(self.sheet_id, name) #no returns?
sheet_view(self.sheet_id) #return view_id
sheet_window(self.sheet_id) #return window_id

view_add_phantom(self.view_id, key, region, content, layout, on_navigate) #returns same as hl api
view_add_regions(self.view_id, key, regions, scope, icon, flags, annotations, annotation_color, on_navigate, on_close) #no returns?
view_assign_syntax(self.view_id, syntax) #no returns?
view_begin_edit(self.view_id, edit_token, cmd, args) #no returns?
view_buffer_id(self.view_id) #returns same as hl api
view_cached_substr(self.view_id, x, x + 1) #return s
view_cached_substr(self.view_id, x.a, x.b) #returns same as hl api
view_change_count(self.view_id) #returns same as hl api
view_change_id(self.view_id) #returns same as hl api
view_classify(self.view_id, pt) #returns same as hl api
view_clear_undo_stack(self.view_id) #no returns?
view_clones(self.view_id) #no returns?
view_command_history(self.view_id, delta, modifying_only) #returns same as hl api
view_context_backtrace(self.view_id, pt) #returns same as hl api
view_element(self.view_id) #return e
view_em_width(self.view_id) #returns same as hl api
view_encoding(self.view_id) #returns same as hl api
view_end_edit(self.view_id, edit.edit_token) #no returns?
view_erase(self.view_id, edit.edit_token, r) #no returns?
view_erase_phantom(self.view_id, pid) #no returns?
view_erase_phantoms(self.view_id, key) #no returns?
view_erase_regions(self.view_id, key) #no returns?
view_erase_status(self.view_id, key) #no returns?
view_expand_by_class(self.view_id, x, x, classes, separators) #returns same as hl api
view_expand_by_class(self.view_id, x.a, x.b, classes, separators) #returns same as hl api
view_export_to_html(self.view_id, regions, options) #returns same as hl api
view_extract_completions(self.view_id, prefix, tp) #returns same as hl api
view_extract_scope(self.view_id, pt) #returns same as hl api
view_extract_tokens_with_scopes(self.view_id, r.begin(), r.end()) #returns same as hl api
view_file_name(self.view_id) #return name
view_find(self.view_id, pattern, start_pt, flags) #returns same as hl api
view_find_all(self.view_id, pattern, flags) #returns same as hl api
view_find_all_results(self.view_id) #returns same as hl api
view_find_all_results_with_text(self.view_id) #returns same as hl api
view_find_all_with_contents(self.view_id, pattern, flags, fmt) #return results
view_find_by_class(self.view_id, pt, forward, classes, separators) #returns same as hl api
view_find_by_selector(self.view_id, selector) #returns same as hl api
view_fold_region(self.view_id, x) #returns same as hl api
view_fold_regions(self.view_id, x) #returns same as hl api
view_folded_regions(self.view_id) #returns same as hl api
view_full_line_from_point(self.view_id, x) #returns same as hl api
view_full_line_from_region(self.view_id, x) #returns same as hl api
view_get_name(self.view_id) #returns same as hl api
view_get_overwrite_status(self.view_id) #returns same as hl api
view_get_regions(self.view_id, key) #returns same as hl api
view_get_status(self.view_id, key) #returns same as hl api
view_has_non_empty_selection_region(self.view_id) #returns same as hl api
view_hide_popup(self.view_id) #no returns?
view_indentation_level(self.view_id, pt) #returns same as hl api
view_indented_region(self.view_id, pt) #returns same as hl api
view_indexed_references(self.view_id) #returns same as hl api
view_indexed_symbol_regions(self.view_id, type) #returns same as hl api
view_indexed_symbols(self.view_id) #returns same as hl api
view_insert(self.view_id, edit.edit_token, pt, text) #returns same as hl api
view_is_auto_complete_visible(self.view_id) #returns same as hl api
view_is_dirty(self.view_id) #returns same as hl api
view_is_folded(self.view_id, sr) #returns same as hl api
view_is_in_edit(self.view_id) #returns same as hl api
view_is_loading(self.view_id) #returns same as hl api
view_is_popup_visible(self.view_id) #returns same as hl api
view_is_primary(self.view_id) #returns same as hl api
view_is_read_only(self.view_id) #returns same as hl api
view_is_scratch(self.view_id) #returns same as hl api
view_layout_extents(self.view_id) #returns same as hl api
view_layout_to_text(self.view_id, xy) #returns same as hl api
view_layout_to_window(self.view_id, xy) #returns same as hl api
view_line_endings(self.view_id) #returns same as hl api
view_line_from_point(self.view_id, x) #returns same as hl api
view_line_from_region(self.view_id, x) #returns same as hl api
view_line_height(self.view_id) #returns same as hl api
view_lines(self.view_id, r) #returns same as hl api
view_match_selector(self.view_id, pt, selector) #returns same as hl api
view_meta_info(self.view_id, key, pt) #returns same as hl api
view_preserve_auto_complete_on_focus_lost(self.view_id) #no returns?
view_query_phantoms(self.view_id, [pid]) #returns same as hl api
view_query_phantoms(self.view_id, pids) #returns same as hl api
view_replace(self.view_id, edit.edit_token, r, text) #no returns?
view_reset_reference_document(self.view_id) #no returns?
view_retarget(self.view_id, new_fname) #no returns?
view_row_col(self.view_id, tp) #returns same as hl api
view_row_col_utf16(self.view_id, tp) #returns same as hl api
view_row_col_utf8(self.view_id, tp) #returns same as hl api
view_run_command(self.view_id, cmd, args) #no returns?
view_scope_name(self.view_id, pt) #returns same as hl api
view_score_selector(self.view_id, pt, selector) #returns same as hl api
view_selection_add_point(self.view_id, x) #no returns?
view_selection_add_region(self.view_id, x.a, x.b, x.xpos) #no returns?
view_selection_clear(self.view_id) #no returns?
view_selection_contains(self.view_id, region.a, region.b) #returns same as hl api
view_selection_erase(self.view_id, index) #no returns?
view_selection_get(self.view_id, i) #no returns?
view_selection_get(self.view_id, index) #return r
view_selection_size(self.view_id) #returns same as hl api
view_selection_subtract_region(self.view_id, region.a, region.b) #no returns?
view_set_encoding(self.view_id, encoding_name) #returns same as hl api
view_set_line_endings(self.view_id, line_ending_name) #returns same as hl api
view_set_name(self.view_id, name) #no returns?
view_set_overwrite_status(self.view_id, value) #no returns?
view_set_read_only(self.view_id, read_only) #returns same as hl api
view_set_reference_document(self.view_id, reference) #no returns?
view_set_scratch(self.view_id, scratch) #returns same as hl api
view_set_status(self.view_id, key, value) #no returns?
view_set_viewport_position(self.view_id, xy, animate) #returns same as hl api
view_settings(self.view_id) #return something
view_sheet_id(self.view_id) #returns same as hl api
view_show_point(self.view_id, x, show_surrounds, keep_to_left, animate) #returns same as hl api
view_show_point_at_center(self.view_id, x, animate) #returns same as hl api
view_show_popup(self.view_id, location, content, flags, max_width, max_height, on_navigate, on_hide) #no returns?
view_show_popup_table(self.view_id, items, on_select, flags, -1) #returns same as hl api
view_show_region(self.view_id, i, show_surrounds, keep_to_left, animate) #returns same as hl api
view_show_region(self.view_id, x, show_surrounds, keep_to_left, animate) #returns same as hl api
view_show_region_at_center(self.view_id, x, animate) #returns same as hl api
view_size(self.view_id) #returns same as hl api
view_split_by_newlines(self.view_id, r) #returns same as hl api
view_style(self.view_id) #returns same as hl api
view_style_for_scope(self.view_id, scope) #returns same as hl api
view_symbol_regions(self.view_id) #returns same as hl api
view_symbols(self.view_id) #returns same as hl api
view_text_point(self.view_id, row, col, clamp_column) #returns same as hl api
view_text_point_utf16(self.view_id, row, col_utf16, clamp_column) #returns same as hl api
view_text_point_utf8(self.view_id, row, col_utf8, clamp_column) #returns same as hl api
view_text_to_layout(self.view_id, tp) #returns same as hl api
view_transform_region_from(self.view_id, r, when) #returns same as hl api
view_unfold_region(self.view_id, x) #returns same as hl api
view_unfold_regions(self.view_id, x) #returns same as hl api
view_update_popup_content(self.view_id, content) #no returns?
view_viewport_extents(self.view_id) #returns same as hl api
view_viewport_position(self.view_id) #returns same as hl api
view_visible_region(self.view_id) #returns same as hl api
view_window(self.view_id) #return window_id
view_window_to_layout(self.view_id, xy) #returns same as hl api
view_word_from_point(self.view_id, x) #returns same as hl api
view_word_from_region(self.view_id, x) #returns same as hl api

window_active_group(self.window_id) #returns same as hl api
window_active_panel(self.window_id) #return name
window_active_sheet(self.window_id) #return sheet_id
window_active_sheet_in_group(self.window_id, group) #return sheet_id
window_active_view(self.window_id) #return view_id
window_active_view_in_group(self.window_id, group) #return view_id
window_bring_to_front(self.window_id) #no returns?
window_close_file(window_id, self.view_id, on_close) #returns same as hl api
window_create_output_panel(self.window_id, name, unlisted) #no returns?
window_destroy_output_panel(self.window_id, name) #no returns?
window_extract_variables(self.window_id) #returns same as hl api
window_file_history(self.window_id) #returns same as hl api
window_find_open_file(self.window_id, fname) #return view_id
window_find_output_panel(self.window_id, name) #return view_id
window_focus_group(self.window_id, idx) #no returns?
window_focus_sheet(self.window_id, sheet.sheet_id) #no returns?
window_focus_view(self.window_id, view.view_id) #no returns?
window_folders(self.window_id) #returns same as hl api
window_get_layout(self.window_id) #returns same as hl api
window_get_project_data(self.window_id) #returns same as hl api
window_get_sheet_index(self.window_id, sheet.sheet_id) #returns same as hl api
window_get_view_index(self.window_id, view.view_id) #returns same as hl api
window_is_ui_element_visible(self.window_id, UI_ELEMENT_MENU) #returns same as hl api
window_is_ui_element_visible(self.window_id, UI_ELEMENT_MINIMAP) #returns same as hl api
window_is_ui_element_visible(self.window_id, UI_ELEMENT_SIDE_BAR) #returns same as hl api
window_is_ui_element_visible(self.window_id, UI_ELEMENT_STATUS_BAR) #returns same as hl api
window_is_ui_element_visible(self.window_id, UI_ELEMENT_TABS) #returns same as hl api
window_lookup_references(self.window_id, sym) #returns same as hl api
window_lookup_references_in_open_files(self.window_id, sym) #returns same as hl api
window_lookup_symbol(self.window_id, sym) #returns same as hl api
window_lookup_symbol_in_open_files(self.window_id, sym) #returns same as hl api
window_move_sheets_to_group(self.window_id, sheet_ids, group, insertion_idx, select) #no returns?
window_new_file(self.window_id, flags, syntax) #no returns?
window_new_html_sheet(self.window_id, name, contents, flags, group) #return text?
window_num_groups(self.window_id) != 0 #returns same as hl api
window_num_groups(self.window_id) #returns same as hl api
window_open_file(self.window_id, fname, flags, group) #no returns?
window_panels(self.window_id) #returns same as hl api
window_project_file_name(self.window_id) #return name
window_run_command(self.window_id, cmd, args) #no returns?
window_select_sheets(self.window_id, [s.sheet_id for s in sheets]) #no returns?
window_selected_sheets(self.window_id) #return sheet_ids
window_selected_sheets_in_group(self.window_id, group) #return sheet_ids
window_set_layout(self.window_id, layout) #no returns?
window_set_project_data(self.window_id, v) #no returns?
window_set_sheet_index(self.window_id, sheet.sheet_id, group, idx) #no returns?
window_set_ui_element_visible(self.window_id, UI_ELEMENT_MENU, flag) #no returns?
window_set_ui_element_visible(self.window_id, UI_ELEMENT_MINIMAP, flag) #no returns?
window_set_ui_element_visible(self.window_id, UI_ELEMENT_SIDE_BAR, flag) #no returns?
window_set_ui_element_visible(self.window_id, UI_ELEMENT_STATUS_BAR, flag) #no returns?
window_set_ui_element_visible(self.window_id, UI_ELEMENT_TABS, flag) #no returns?
window_set_view_index(self.window_id, view.view_id, group, idx) #no returns?
window_settings(self.window_id) #no returns?
window_sheets(self.window_id) #return sheet_ids
window_sheets_in_group(self.window_id, group) #return sheet_ids
window_show_input_panel(self.window_id, caption, initial_text, on_done, on_change, on_cancel) #no returns?
window_show_quick_panel(self.window_id, item_tuples, on_select, on_highlight, flags, selected_index, placeholder or '') #no returns?
window_status_message(self.window_id, msg) #no returns?
window_symbol_locations(self.window_id, sym, source, type, kind_id, letter) #returns same as hl api
window_system_handle(self.window_id) #returns same as hl api
window_template_settings(self.window_id) #no returns?
window_transient_sheet_in_group(self.window_id, group) #return sheet_id
window_transient_view_in_group(self.window_id, group) #return view_id
window_views(self.window_id, include_transient) #return view_ids
window_views_in_group(self.window_id, group) #return view_ids
window_workspace_file_name(self.window_id) #return name


### All LL API calls in sublime_plugin.py

can_accept_input(self.name(), args) #returns bool
notify_application_commands(create_application_commands()) #no returns?

buffer_add_text_listener(buffer.buffer_id, self) #returns id?
buffer_clear_text_listener(self.buffer.buffer_id, self.__key) #no returns?

view_can_accept_input(self.view.id(), self.name(), args) # returns bool
view_set_completions(self.view_id, self.req_id, (self.completions, self.flags)) #returns?
view_window(self.view.id(), kwargs) #returns?

window_active_view(w.window_id) #returns view_id
window_can_accept_input(self.window.id(), self.name(), args) # returns bool
window_run_command(self.window.id(), kwargs) #returns?
