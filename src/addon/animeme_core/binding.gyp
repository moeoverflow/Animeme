{
  'targets': [
    {
      'target_name': 'animeme_core',
      'defines': [ 'V8_DEPRECATION_WARNINGS=1' ],
      'include_dirs' : [
        "src",
        "<!(node -e \"require('nan')\")"
      ],
      'sources': [
        'src/binding.cc'
      ]
    }
  ]
}
