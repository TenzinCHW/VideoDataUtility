from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=DGhPGH2YROA')
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age_restricted', 'caption_tracks', 'captions', 'embed_html', 'embed_url', 'fmt_streams', 'init', 'initialize_caption_objects', 'initialize_stream_objects', 'js', 'js_url', 'player_config_args', 'prefetch', 'prefetch_init', 'register_on_complete_callback', 'register_on_progress_callback', 'stream_monostate', 'streams', 'thumbnail_url', 'title', 'vid_info', 'vid_info_url', 'video_id', 'watch_html', 'watch_url']
print('age restrict', yt.age_restricted)
print('caption_tracks', yt.caption_tracks)
print('cations', yt.captions)
#print('embed html', yt.embed_html) # this is the html of the page
print('embed url', yt.embed_url)
print('fmt streams', yt.fmt_streams)
print('player config args', yt.player_config_args.keys())
print('stream monostate', yt.stream_monostate)
print('thumbnail url', yt.thumbnail_url)
print('title', yt.title)
print('vid info', yt.vid_info)
print('vid info url', yt.vid_info_url)
print('video id', yt.video_id)
#print('watch html', yt.watch_html) # more html
print('watch url', yt.watch_url)

formats = yt.streams.filter(progressive=True).order_by('resolution').all()
item = formats[0]
print('has video', item.includes_video_track)
print('has audio', item.includes_audio_track)
print('is progressive', item.is_progressive)
print('file size', item.filesize)
print('itag', item.itag)
print('default filename', item.default_filename)
print('mime type', item.mime_type)
print('parse codecs', item.parse_codecs)
print('player config args', item.player_config_args.keys())
print('quality', item.quality)
print('res', item.res)
print('resolution', item.resolution)
print('s', item.s)
print('sp', item.sp)
print('type', item.type)
print('subtype', item.subtype)
print('url', item.url)
print('video codec', item.video_codec)

#item.download('../data/video/unprocessed/')

#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_monostate', 'abr', 'audio_codec', 'codecs', 'default_filename', 'download', 'filesize', 'fmt_profile', 'fps', 'includes_audio_track', 'includes_video_track', 'is_3d', 'is_adaptive', 'is_hdr', 'is_live', 'is_progressive', 'itag', 'mime_type', 'on_complete', 'on_progress', 'parse_codecs', 'player_config_args', 'quality', 'res', 'resolution', 's', 'set_attributes_from_dict', 'sp', 'subtype', 'type', 'url', 'video_codec']


#item.fmt_profile = {'fps': 30, 'abr': '24kbps', 'is_3d': False, 'is_live': False, 'is_hdr': False, 'resolution': '144p'}
#has video True
#has audio True
#is progressive True
#file size 2052740
#itag 17
#default filename Lindsey Stirling - The Greatest Showman Medley.3gpp
#mime type video/3gpp
#parse codecs <bound method Stream.parse_codecs of <Stream: itag="17" mime_type="video/3gpp" res="144p" fps="30fps" vcodec="mp4v.20.3" acodec="mp4a.40.2">>
#player config args dict_keys(['show_content_thumbnail', 'ismb', 'cver', 'serialized_ad_ux_config', 'ucid', 'itct', 'title', 'dclk', 'midroll_prefetch_size', 'idpj', 'ad_logging_flag', 'external_play_video', 'avg_rating', 'remarketing_url', 'ad_preroll', 'pyv_ad_channel', 'tag_for_child_directed', 'is_listed', 'url_encoded_fmt_stream_map', 'ad_device', 'enablecsi', 'trueview', 'view_count', 'fexp', 'ad3_module', 'video_id', 'cid', 'no_get_video_log', 'fade_in_start_milliseconds', 'loeid', 'afv_ad_tag', 'encoded_ad_safety_reason', 'relative_loudness', 'of', 'enabled_engage_types', 'fmt_list', 'innertube_api_version', 'loaderUrl', 'gpt_migration', 'author', 'xhr_apiary_host', 'vss_host', 'ad_slots', 'player_response', 'ppv_remarketing_url', 'show_pyv_in_related', 'oid', 'rmktEnabled', 'plid', 'invideo', 'videostats_playback_base_url', 'loudness', 'hl', 'core_dbp', 'focEnabled', 'ldpj', 'sffb', 'host_language', 'player_error_log_fraction', 'mpu', 'allow_embed', 'c', 'allow_below_the_player_companion', 'account_playback_token', 'uid', 'fade_out_start_milliseconds', 'baseUrl', 'allow_ratings', 'iv_invideo_url', 'csi_page_type', 'allow_html5_ads', 'enablejsapi', 'fflags', 'tmi', 'mpvid', 'iv_load_policy', 'thumbnail_url', 'ptchn', 'gut_tag', 'pltype', 'adsense_video_doc_id', 'storyboard_spec', 'midroll_freqcap', 'fade_in_duration_milliseconds', 'cl', 'as_launched_in_country', 'keywords', 'watermark', 'innertube_context_client_version', 'vm', 'atc', 'adaptive_fmts', 'vid', 'ptk', 'apply_fade_on_midrolls', 'ad_tag', 'swf_player_response', 'shortform', 't', 'ad_flags', 'eventid', 'gapi_hint_params', 'fade_out_duration_milliseconds', 'instream', 'afv', 'apiary_host_firstparty', 'length_seconds', 'vmap', 'token', 'timestamp', 'innertube_api_key', 'probe_url', 'ssl', 'cr', 'instream_long', 'iv3_module', 'dbp', 'apiary_host'])
#quality small
#res None
#resolution 144p
#s 1A948E90A5D321A1E8661BB6E8B972C333A5BF83.800360D81A6F03C2F07617F815F52D75122266722
#sp signature
#type video
#subtype 3gpp
#url https://r1---sn-nu5gi0c-npoee.googlevideo.com/videoplayback?clen=2052740&mt=1521566365&mv=m&pl=24&ei=JUOxWru3JI6togPxs6n4Cg&ms=au,rdu&mm=31,29&mn=sn-nu5gi0c-npoee,sn-npoeene7&mime=video/3gpp&key=yt6&c=WEB&gir=yes&fvip=1&expire=1521588101&initcwndbps=2537500&ipbits=0&sparams=clen,dur,ei,gir,id,initcwndbps,ip,ipbits,itag,lmt,mime,mm,mn,ms,mv,pl,requiressl,source,expire&source=youtube&dur=208.886&id=o-AOoMclbdtM3wK-7UZq3h752dtHNr-ZkazgV5Wbwcyrkg&itag=17&lmt=1519764347981610&requiressl=yes&ip=202.94.70.51&signature=AA948E90A5D321A1E8661BB6E8B972C333A5BF83.800360D8116F03C2F07617F815F52D7512226672
#video codec mp4v.20.3
