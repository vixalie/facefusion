from typing import List, Optional

import gradio

import facefusion.globals
from facefusion import wording
from facefusion.uis import choices as uis_choices

COMMON_OPTIONS_CHECKBOX_GROUP : Optional[gradio.Checkboxgroup] = None


def render() -> None:
	global COMMON_OPTIONS_CHECKBOX_GROUP

	value = []
	if facefusion.globals.keep_temp:
		value.append('keep-temp')
	if facefusion.globals.skip_audio:
		value.append('skip-audio')
	if facefusion.globals.skip_download:
		value.append('skip-download')
	if facefusion.globals.allow_nsfw:
		value.append('allow-nsfw')
	COMMON_OPTIONS_CHECKBOX_GROUP = gradio.Checkboxgroup(
		label = wording.get('uis.common_options_checkbox_group'),
		choices = uis_choices.common_options,
		value = value
	)


def listen() -> None:
	COMMON_OPTIONS_CHECKBOX_GROUP.change(update, inputs = COMMON_OPTIONS_CHECKBOX_GROUP)


def update(common_options : List[str]) -> None:
	facefusion.globals.allow_nsfw = 'allow-nsfw' in common_options
	facefusion.globals.keep_temp = 'keep-temp' in common_options
	facefusion.globals.skip_audio = 'skip-audio' in common_options
	facefusion.globals.skip_download = 'skip-download' in common_options
