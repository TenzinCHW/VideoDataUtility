from pytube import YouTube

# Useful site for itags meanings https://www.genyoutube.net/formats-resolution-youtube-videos.html

yt = YouTube('https://www.youtube.com/watch?v=tjPW04Q139o')
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age_restricted', 'caption_tracks', 'captions', 'embed_html', 'embed_url', 'fmt_streams', 'init', 'initialize_caption_objects', 'initialize_stream_objects', 'js', 'js_url', 'player_config_args', 'prefetch', 'prefetch_init', 'register_on_complete_callback', 'register_on_progress_callback', 'stream_monostate', 'streams', 'thumbnail_url', 'title', 'vid_info', 'vid_info_url', 'video_id', 'watch_html', 'watch_url']

#print('age restrict', yt.age_restricted)
#print('caption_tracks', yt.caption_tracks)
#print('captions', yt.captions)
##print('embed html', yt.embed_html) # this is the html of the page
#print('embed url', yt.embed_url)
#print('fmt streams', yt.fmt_streams)
#print('player config args', yt.player_config_args.keys())
#print('stream monostate', yt.stream_monostate)
#print('thumbnail url', yt.thumbnail_url)
#print('title', yt.title)
#print('vid info', yt.vid_info)
#print('vid info url', yt.vid_info_url)
print('video id', yt.video_id)
##print('watch html', yt.watch_html) # more html
#print('watch url', yt.watch_url)

#age restrict False
#caption_tracks []
#cations <pytube.query.CaptionQuery object at 0x7fd9c6be1b00>
#embed url https://www.youtube.com/embed/DGhPGH2YROA
#fmt streams [<Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2">, <Stream: itag="43" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp8.0" acodec="vorbis">, <Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2">, <Stream: itag="36" mime_type="video/3gpp" res="240p" fps="30fps" vcodec="mp4v.20.3" acodec="mp4a.40.2">, <Stream: itag="17" mime_type="video/3gpp" res="144p" fps="30fps" vcodec="mp4v.20.3" acodec="mp4a.40.2">, <Stream: itag="313" mime_type="video/webm" res="2160p" fps="30fps" vcodec="vp9">, <Stream: itag="264" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.640032">, <Stream: itag="271" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9">, <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028">, <Stream: itag="248" mime_type="video/webm" res="1080p" fps="30fps" vcodec="vp9">, <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.4d401f">, <Stream: itag="247" mime_type="video/webm" res="720p" fps="30fps" vcodec="vp9">, <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401e">, <Stream: itag="244" mime_type="video/webm" res="480p" fps="30fps" vcodec="vp9">, <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e">, <Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9">, <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d400d">, <Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9">, <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c">, <Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9">, <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2">, <Stream: itag="171" mime_type="audio/webm" abr="128kbps" acodec="vorbis">, <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus">, <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus">, <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus">]
#player config args dict_keys(['eventid', 'pltype', 'atc', 'account_playback_token', 'length_seconds', 'innertube_api_version', 'ad_preroll', 'rmktEnabled', 'fade_out_duration_milliseconds', 'mpvid', 'csi_page_type', 'fade_out_start_milliseconds', 'enablecsi', 'tag_for_child_directed', 'dclk', 'apply_fade_on_midrolls', 'token', 'ad_logging_flag', 'as_launched_in_country', 'vmap', 'iv_load_policy', 'remarketing_url', 'ad_flags', 'gapi_hint_params', 'iv_invideo_url', 'focEnabled', 'keywords', 'timestamp', 'midroll_prefetch_size', 'show_content_thumbnail', 'cr', 'loudness', 'gpt_migration', 'iv3_module', 'trueview', 'ptchn', 'sffb', 'ismb', 'ad_slots', 'innertube_api_key', 'afv', 'player_error_log_fraction', 'instream', 'apiary_host', 'fade_in_start_milliseconds', 'ad_tag', 'video_id', 'ucid', 'vid', 'allow_embed', 'url_encoded_fmt_stream_map', 'allow_below_the_player_companion', 'allow_html5_ads', 'itct', 'adsense_video_doc_id', 'gut_tag', 'of', 'fade_in_duration_milliseconds', 'core_dbp', 'apiary_host_firstparty', 'ldpj', 'loeid', 'external_play_video', 'enabled_engage_types', 'instream_long', 'enablejsapi', 'ptk', 'ad_device', 'xhr_apiary_host', 'invideo', 'plid', 'shortform', 'vm', 'c', 'storyboard_spec', 'afv_ad_tag', 'is_listed', 'ad3_module', 'dbp', 'ssl', 'view_count', 'hl', 'innertube_context_client_version', 'serialized_ad_ux_config', 'fflags', 'host_language', 'adaptive_fmts', 'encoded_ad_safety_reason', 'tmi', 'vss_host', 'loaderUrl', 'oid', 'author', 'uid', 'avg_rating', 'show_pyv_in_related', 'cid', 'thumbnail_url', 'cver', 'baseUrl', 'mpu', 'player_response', 'pyv_ad_channel', 'relative_loudness', 'swf_player_response', 'idpj', 'allow_ratings', 'videostats_playback_base_url', 't', 'title', 'ppv_remarketing_url', 'watermark', 'fexp', 'cl', 'fmt_list', 'midroll_freqcap', 'no_get_video_log'])
#stream monostate {'on_progress': None, 'on_complete': None}
#thumbnail url https://i.ytimg.com/vi/DGhPGH2YROA/default.jpg
#title Lindsey Stirling - The Greatest Showman Medley
#vid info {'errorcode': '2', 'status': 'fail', 'reason': 'Invalid parameters.'}
#vid info url https://youtube.com/get_video_info?video_id=DGhPGH2YROA&el=%24el&ps=default&eurl=https%253A%2F%2Fyoutube.com%2Fwatch%253Fv%253DDGhPGH2YROA&hl=en_US&t=%252C%2522t%2522%253A%25221%2522
#video id DGhPGH2YROA
#watch url https://youtube.com/watch?v=DGhPGH2YROA

cap = yt.captions
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'all', 'captions', 'get_by_language_code', 'lang_code_index']
#print('captions captions', cap.captions)
print('captions all', cap.all()) # same as cap.captions
#print('captions get by lang code', cap.get_by_language_code)
#print('captions lang code index', cap.lang_code_index)

#realcaption = cap.captions[0] # what if it's empty lol
#print(realcaption)
#print(dir(cap.captions[0]))
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'code', 'float_to_srt_time_format', 'generate_srt_captions', 'name', 'url', 'xml_caption_to_srt', 'xml_captions']
#print('cap code', realcaption.code)
#print('cap float to srt time format', realcaption.float_to_srt_time_format)
#print('cap gen srt captions', realcaption.generate_srt_captions)
#print('cap name', realcaption.name)
#print('cap url', realcaption.url)
#print('cap xml cap to srt', realcaption.xml_caption_to_srt(realcaption.xml_captions))
#print('cap xml captions', realcaption.xml_captions)

#with open('xml', 'w') as f:  # srt takes less memory
#    f.write(realcaption.xml_captions)
#with open('srt', 'w') as f:
#    f.write(realcaption.generate_srt_captions())

formats = yt.streams.filter(progressive=True).order_by('resolution').all()
item = formats[0]
#print('has video', item.includes_video_track)
#print('has audio', item.includes_audio_track)
#print('is progressive', item.is_progressive)
#print('file size', item.filesize)
#print('itag', item.itag)
#print('default filename', item.default_filename)
#print('mime type', item.mime_type)
#print('parse codecs', item.parse_codecs)
#print('player config args', item.player_config_args.keys())
#print('quality', item.quality)
#print('res', item.res)
#print('resolution', item.resolution)
#print('s', item.s)
#print('sp', item.sp)
#print('type', item.type)
#print('subtype', item.subtype)
#print('url', item.url)
#print('video codec', item.video_codec)

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

