class PrefixLengthError(Exception):
    pass

class PrefixMissingLengthError(Exception):
    pass


class PrefixKeyError(Exception):
    pass

class Prefix:
    
    
    def __init__(self, template=None, length=None, 
                 **template_opts):
        
        if length:
            template_opts = {
                k: v for k,v in template_opts.items() if v is not None}
            try:
                self.prefix = template.format(**template_opts)
            
            except KeyError as e:
                raise PrefixKeyError(f'Missing template value for \'{e}\'.Got options={template_opts}' )
        
        
               
            if len(self.prefix) != length:
                raise PrefixLengthError(
                    f'Invalid prefix \' {self.prefix}\'.'
                    f'Got length == {len(self.prefix)}. Expected{length}. ')
        else:
            
            raise PrefixMissingLengthError(f'Length is empty or None')
            
        
        
            
    def __str__(self):
        return self.prefix
            