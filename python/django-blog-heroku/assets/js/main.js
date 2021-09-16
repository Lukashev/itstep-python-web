$(document).ready(function(){

   scroller.init();

   const navLinks = $('.nav-link')
   const categoryLinks = $('.category-link')
   const currentPath = window.location.pathname.split('/')
   const basePath = currentPath[1]
   const secondPath = currentPath[2]

   const navLink = [...navLinks].find(link => {
         const href = $(link).attr('href')
         return href.includes(basePath)
   })
   if (basePath === 'article') {
        $(navLinks[0]).addClass('active')
   } else {
        $(navLink).addClass('active')
   }

   if (categoryLinks) {
        const categoryLink = [...categoryLinks].find(link => {
             const href = $(link).attr('href')
             return href.includes(secondPath)
        })
        if (basePath === '') {
            $(categoryLinks[0]).parent().addClass('active')
        } else {
            $(categoryLink).parent().addClass('active')
        }
   }

})