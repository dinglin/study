{
  if( $1=="use" ){
    #print $0
  }else if( $1=="#" && $2=="Query_time:"){
    #print $0
  }else if( $1=="SELECT"){
    #print $0
  }else if( $1=="INSERT"){
    print index($0,"# php")
  }else if( $1=="DELETE"){
    #print $0
  }else if( $1=="UPDATE"){
    #print $0
  }

 
}
