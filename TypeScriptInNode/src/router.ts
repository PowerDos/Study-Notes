export default (controller: any) => {
    return {
        'get /': controller.home.index,
        'get /mypage': controller.user.index,
        'get /mysetting': controller.user.setting
    }
}