from portfolio.models import *
from annoying.decorators import render_to, ajax_request
from django.shortcuts import get_object_or_404

@ajax_request
def galleries(request):
	galleries = Gallery.objects.all()
	response = []
	for gallery in galleries:
		gallery_items = []
		for gi in gallery.galleryitem_set.all():
			if gi.content_type.name == 'video':
				format = VideoFormat.objects.filter(video=gi.content_object).all()
				fr = []
				for f in format:
					fr.append({'id':f.id, 'file':f.video_file.url or None,\
								'format': f.format })
				o = {gi.content_type.name: {'id': gi.object_id,\
					 'formats': fr, 'context': gi.context} }
			else:
				o = {gi.content_type.name: {'id': gi.object_id,\
					 'file':gi.content_object.image.url, 'context': gi.context} }
			gallery_items.append(o)
		gal = {}
		gal['id'] = gallery.id
		gal['title'] = gallery.title
		gal['description'] = gallery.description
		gal['items'] = gallery_items
		response.append(gal)
	return {'galleries': response}

@ajax_request
def gallery(request, gallery_id):
	gallery = get_object_or_404(Gallery, id=gallery_id)
	gallery_items = []
	for gi in gallery.galleryitem_set.all():
		if gi.content_type.name == 'video':
			format = VideoFormat.objects.filter(video=gi.content_object).all()
			fr = []
			for f in format:
				fr.append({'id':f.id, 'file':f.video_file.url or None,\
							'format': f.format })
			o = {gi.content_type.name: {'id': gi.object_id,\
				 'formats': fr, 'context': gi.context} }
		else:
			o = {gi.content_type.name: {'id': gi.object_id,\
				 'file':gi.content_object.image.url, 'context': gi.context} }
		gallery_items.append(o)
	response = {}
	response['id'] = gallery.id
	response['title'] = gallery.title
	response['description'] = gallery.description
	response['items'] = gallery_items

	return {'gallery': response}